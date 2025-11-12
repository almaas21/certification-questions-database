#!/usr/bin/env python3
"""
Production-ready web scraper using crawlforai for examtopics.com and similar sites.

Features:
- Robust error handling and logging
- Retry logic with exponential backoff
- Rate limiting to respect target sites
- HTML-to-markdown conversion
- Content validation and quality checks
- Configuration file support
- Batch processing capabilities
- Dry-run mode for testing

Use at your own risk and respect target site terms of service.
"""

from __future__ import annotations

import argparse
import json
import logging
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Optional
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("tools/scraper.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger(__name__)


class ScraperError(Exception):
    """Base exception for scraper errors."""


class ValidationError(ScraperError):
    """Raised when content validation fails."""


class RateLimiter:
    """Simple rate limiter to respect target sites."""

    def __init__(self, min_delay: float = 2.0):
        self.min_delay = min_delay
        self.last_request_time: Optional[float] = None

    def wait(self) -> None:
        """Wait if necessary to respect rate limit."""
        if self.last_request_time is not None:
            elapsed = time.time() - self.last_request_time
            if elapsed < self.min_delay:
                wait_time = self.min_delay - elapsed
                logger.debug(f"Rate limiting: waiting {wait_time:.2f}s")
                time.sleep(wait_time)
        self.last_request_time = time.time()


class ContentValidator:
    """Validates scraped content quality."""

    MIN_CONTENT_LENGTH = 100
    BLOCKED_INDICATORS = [
        "access denied",
        "captcha",
        "forbidden",
        "rate limit",
        "blocked",
        "cloudflare",
    ]

    @classmethod
    def validate(cls, content: str, url: str) -> None:
        """Validate content quality and detect common issues."""
        if not content or len(content.strip()) < cls.MIN_CONTENT_LENGTH:
            raise ValidationError(
                f"Content too short ({len(content)} chars). Minimum: {cls.MIN_CONTENT_LENGTH}"
            )

        content_lower = content.lower()
        for indicator in cls.BLOCKED_INDICATORS:
            if indicator in content_lower:
                raise ValidationError(
                    f"Content appears to be blocked or restricted (found: '{indicator}')"
                )

        logger.info(f"Content validation passed: {len(content)} chars from {url}")


def convert_html_to_markdown(html_content: str) -> str:
    """Convert HTML to markdown using html2text if available."""
    try:
        import html2text

        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.ignore_emphasis = False
        h.body_width = 0  # Don't wrap lines
        markdown = h.handle(html_content)
        logger.debug("Successfully converted HTML to markdown using html2text")
        return markdown
    except ImportError:
        logger.warning("html2text not available, using basic conversion")
        # Basic fallback conversion
        if "<html" in html_content.lower():
            return f"<!-- Raw HTML content -->\n\n```html\n{html_content}\n```\n"
        return html_content


def try_import_and_scrape(url: str, timeout: int = 30) -> Optional[str]:
    """Try to scrape using the crawlforai Python library."""
    try:
        import crawlforai

        logger.info(f"Attempting to scrape {url} using crawlforai library")

        # Try various API patterns
        if hasattr(crawlforai, "scrape"):
            logger.debug("Using crawlforai.scrape() API")
            result = crawlforai.scrape(url, timeout=timeout)
            return result if isinstance(result, str) else str(result)

        if hasattr(crawlforai, "Crawler"):
            logger.debug("Using crawlforai.Crawler API")
            crawler = crawlforai.Crawler()
            if hasattr(crawler, "scrape"):
                result = crawler.scrape(url, timeout=timeout)
                return result if isinstance(result, str) else str(result)

        logger.warning("crawlforai library imported but no known API found")
        return None

    except ImportError:
        logger.debug("crawlforai library not installed")
        return None
    except Exception as e:
        logger.error(f"Error using crawlforai library: {type(e).__name__}: {e}")
        return None


def try_cli_and_scrape(url: str, timeout: int = 30) -> Optional[str]:
    """Try to scrape using the crawlforai CLI."""
    exe = shutil.which("crawlforai")
    if not exe:
        logger.debug("crawlforai CLI not found in PATH")
        return None

    logger.info(f"Attempting to scrape {url} using crawlforai CLI")

    # Try various CLI command patterns
    candidates = [
        [exe, "scrape", url],
        [exe, "crawl", url],
        [exe, url],
        [exe, "--url", url],
        [exe, "-u", url],
    ]

    for cmd in candidates:
        try:
            logger.debug(f"Trying CLI command: {' '.join(cmd)}")
            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=timeout,
                check=False,
                text=True,
            )

            if result.returncode == 0 and result.stdout.strip():
                logger.info(f"CLI command succeeded: {' '.join(cmd)}")
                return result.stdout

            if result.stderr:
                logger.debug(f"CLI stderr: {result.stderr[:500]}")

        except subprocess.TimeoutExpired:
            logger.warning(f"CLI command timed out after {timeout}s: {' '.join(cmd)}")
        except FileNotFoundError:
            logger.debug("CLI executable not found")
            return None
        except Exception as e:
            logger.debug(f"CLI command failed: {type(e).__name__}: {e}")

    logger.warning("All CLI command attempts failed")
    return None


def scrape_with_retry(
    url: str,
    max_retries: int = 3,
    initial_delay: float = 1.0,
    prefer_cli: bool = False,
    timeout: int = 30,
) -> str:
    """Scrape URL with exponential backoff retry logic."""
    delay = initial_delay

    for attempt in range(1, max_retries + 1):
        try:
            logger.info(f"Scrape attempt {attempt}/{max_retries} for {url}")

            content: Optional[str] = None

            if prefer_cli:
                content = try_cli_and_scrape(url, timeout)
                if content is None:
                    logger.debug("CLI failed, trying library")
                    content = try_import_and_scrape(url, timeout)
            else:
                content = try_import_and_scrape(url, timeout)
                if content is None:
                    logger.debug("Library failed, trying CLI")
                    content = try_cli_and_scrape(url, timeout)

            if content:
                # Validate content
                ContentValidator.validate(content, url)
                logger.info(f"Successfully scraped {url} on attempt {attempt}")
                return content

            # No content retrieved
            if attempt < max_retries:
                logger.warning(f"Attempt {attempt} failed, retrying in {delay}s...")
                time.sleep(delay)
                delay *= 2  # Exponential backoff
            else:
                raise ScraperError(
                    "Could not scrape content using crawlforai library or CLI. "
                    "Install with: pip install crawlforai"
                )

        except ValidationError as e:
            logger.error(f"Content validation failed on attempt {attempt}: {e}")
            if attempt < max_retries:
                logger.warning(f"Retrying in {delay}s...")
                time.sleep(delay)
                delay *= 2
            else:
                raise
        except Exception as e:
            logger.error(f"Unexpected error on attempt {attempt}: {type(e).__name__}: {e}")
            if attempt < max_retries:
                logger.warning(f"Retrying in {delay}s...")
                time.sleep(delay)
                delay *= 2
            else:
                raise ScraperError(f"Scraping failed after {max_retries} attempts") from e

    raise ScraperError(f"Scraping failed after {max_retries} attempts")


def write_output(
    path: Path, content: str, url: str, metadata: Optional[dict[str, Any]] = None
) -> None:
    """Write scraped content to file with metadata."""
    path.parent.mkdir(parents=True, exist_ok=True)

    # Add metadata header
    header = f"""<!-- 
Scraped from: {url}
Scraped at: {datetime.now().isoformat()}
Scraper: crawlforai_scraper.py
-->

"""

    if metadata:
        header += f"<!-- Metadata: {json.dumps(metadata, indent=2)} -->\n\n"

    full_content = header + content

    path.write_text(full_content, encoding="utf-8")
    logger.info(f"Successfully wrote {len(full_content)} bytes to {path}")


def load_config(config_path: Optional[Path] = None) -> dict[str, Any]:
    """Load configuration from YAML or JSON file."""
    if config_path and config_path.exists():
        try:
            import yaml

            with open(config_path, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f)
                logger.info(f"Loaded configuration from {config_path}")
                return config or {}
        except ImportError:
            logger.debug("PyYAML not installed, trying JSON")
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    config = json.load(f)
                    logger.info(f"Loaded configuration from {config_path}")
                    return config
            except json.JSONDecodeError as e:
                logger.error(f"Invalid JSON in config file: {e}")
                return {}
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            return {}
    return {}


def main(argv: Optional[list[str]] = None) -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Production-ready web scraper using crawlforai",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("url", nargs="?", help="URL to scrape (e.g., examtopics.com question)")
    parser.add_argument(
        "-o", "--output", help="Output file path (default: scraped/examtopics.md)"
    )
    parser.add_argument("--prefer-cli", action="store_true", help="Prefer crawlforai CLI over library")
    parser.add_argument(
        "--config", type=Path, help="Configuration file (YAML or JSON)"
    )
    parser.add_argument(
        "--batch", type=Path, help="Batch file with URLs (one per line)"
    )
    parser.add_argument(
        "--rate-limit", type=float, default=2.0, help="Minimum delay between requests in seconds (default: 2.0)"
    )
    parser.add_argument(
        "--max-retries", type=int, default=3, help="Maximum retry attempts (default: 3)"
    )
    parser.add_argument(
        "--timeout", type=int, default=30, help="Request timeout in seconds (default: 30)"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Simulate without actually scraping"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose logging"
    )
    parser.add_argument(
        "--convert-html", action="store_true", default=True, help="Convert HTML to markdown (default: True)"
    )

    args = parser.parse_args(argv)

    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Verbose logging enabled")

    # Load configuration
    config = load_config(args.config)

    # Initialize rate limiter
    rate_limiter = RateLimiter(min_delay=args.rate_limit)

    try:
        # Batch processing
        if args.batch:
            if not args.batch.exists():
                logger.error(f"Batch file not found: {args.batch}")
                return 1

            logger.info(f"Processing batch file: {args.batch}")
            urls = [
                line.strip()
                for line in args.batch.read_text(encoding="utf-8").splitlines()
                if line.strip() and not line.strip().startswith("#")
            ]

            if not urls:
                logger.error("No URLs found in batch file")
                return 1

            logger.info(f"Found {len(urls)} URLs to process")

            for i, url in enumerate(urls, 1):
                logger.info(f"Processing {i}/{len(urls)}: {url}")

                if args.dry_run:
                    logger.info(f"[DRY RUN] Would scrape: {url}")
                    continue

                rate_limiter.wait()

                # Generate output path
                parsed = urlparse(url)
                filename = f"{parsed.netloc}_{i}.md".replace("/", "_")
                output_path = Path(args.output or "scraped") / filename

                try:
                    content = scrape_with_retry(
                        url,
                        max_retries=args.max_retries,
                        prefer_cli=args.prefer_cli,
                        timeout=args.timeout,
                    )

                    if args.convert_html and "<html" in content.lower():
                        content = convert_html_to_markdown(content)

                    write_output(
                        output_path,
                        content,
                        url,
                        metadata={"batch_index": i, "total": len(urls)},
                    )

                except (ScraperError, ValidationError) as e:
                    logger.error(f"Failed to scrape {url}: {e}")
                    continue

            logger.info(f"Batch processing complete: {len(urls)} URLs processed")
            return 0

        # Single URL processing
        if not args.url:
            parser.error("URL required (or use --batch for batch processing)")

        url = args.url
        output_path = Path(args.output or "scraped/examtopics.md")

        logger.info(f"Scraping single URL: {url}")

        if args.dry_run:
            logger.info(f"[DRY RUN] Would scrape {url} to {output_path}")
            return 0

        content = scrape_with_retry(
            url,
            max_retries=args.max_retries,
            prefer_cli=args.prefer_cli,
            timeout=args.timeout,
        )

        if args.convert_html and "<html" in content.lower():
            content = convert_html_to_markdown(content)

        write_output(output_path, content, url)

        logger.info("Scraping completed successfully")
        return 0

    except KeyboardInterrupt:
        logger.warning("Interrupted by user")
        return 130
    except Exception as e:
        logger.error(f"Fatal error: {type(e).__name__}: {e}", exc_info=args.verbose)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
