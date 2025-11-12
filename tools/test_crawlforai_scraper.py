#!/usr/bin/env python3
"""
Unit tests for crawlforai_scraper.py

Run with: python -m pytest tools/test_crawlforai_scraper.py -v
"""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, mock_open, patch

import crawlforai_scraper as scraper


class TestContentValidator(unittest.TestCase):
    """Test ContentValidator class."""

    def test_valid_content(self):
        """Test that valid content passes validation."""
        content = "A" * 200
        scraper.ContentValidator.validate(content, "https://example.com")

    def test_content_too_short(self):
        """Test that short content raises ValidationError."""
        content = "Short"
        with self.assertRaises(scraper.ValidationError) as ctx:
            scraper.ContentValidator.validate(content, "https://example.com")
        self.assertIn("too short", str(ctx.exception).lower())

    def test_blocked_content_captcha(self):
        """Test detection of CAPTCHA blocked content."""
        content = "Please complete the CAPTCHA to continue" + "A" * 200
        with self.assertRaises(scraper.ValidationError) as ctx:
            scraper.ContentValidator.validate(content, "https://example.com")
        self.assertIn("blocked", str(ctx.exception).lower())

    def test_blocked_content_access_denied(self):
        """Test detection of access denied content."""
        content = "Access Denied - You do not have permission" + "A" * 200
        with self.assertRaises(scraper.ValidationError) as ctx:
            scraper.ContentValidator.validate(content, "https://example.com")
        self.assertIn("blocked", str(ctx.exception).lower())


class TestRateLimiter(unittest.TestCase):
    """Test RateLimiter class."""

    def test_rate_limiter_initial(self):
        """Test that first request doesn't wait."""
        limiter = scraper.RateLimiter(min_delay=1.0)
        import time

        start = time.time()
        limiter.wait()
        elapsed = time.time() - start
        self.assertLess(elapsed, 0.1)

    def test_rate_limiter_subsequent(self):
        """Test that subsequent requests are rate limited."""
        limiter = scraper.RateLimiter(min_delay=0.5)
        import time

        limiter.wait()
        start = time.time()
        limiter.wait()
        elapsed = time.time() - start
        self.assertGreaterEqual(elapsed, 0.4)


class TestHTMLConversion(unittest.TestCase):
    """Test HTML to markdown conversion."""

    def test_convert_simple_html(self):
        """Test basic HTML conversion."""
        html = "<html><body><h1>Title</h1><p>Content</p></body></html>"
        result = scraper.convert_html_to_markdown(html)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    @patch("crawlforai_scraper.html2text")
    def test_convert_with_html2text(self, mock_html2text):
        """Test conversion when html2text is available."""
        mock_converter = MagicMock()
        mock_converter.handle.return_value = "# Title\n\nContent"
        mock_html2text.HTML2Text.return_value = mock_converter

        html = "<html><body><h1>Title</h1><p>Content</p></body></html>"
        result = scraper.convert_html_to_markdown(html)
        self.assertEqual(result, "# Title\n\nContent")

    def test_convert_plain_text(self):
        """Test that plain text passes through."""
        text = "Plain text content"
        result = scraper.convert_html_to_markdown(text)
        self.assertEqual(result, text)


class TestWriteOutput(unittest.TestCase):
    """Test output writing functionality."""

    def test_write_output_creates_directory(self):
        """Test that output directory is created."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "subdir" / "output.md"
            content = "Test content"
            scraper.write_output(output_path, content, "https://example.com")

            self.assertTrue(output_path.exists())
            self.assertTrue(output_path.parent.exists())

    def test_write_output_includes_metadata(self):
        """Test that metadata is included in output."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "output.md"
            content = "Test content"
            url = "https://example.com/test"
            metadata = {"key": "value"}

            scraper.write_output(output_path, content, url, metadata)

            written_content = output_path.read_text(encoding="utf-8")
            self.assertIn(url, written_content)
            self.assertIn("Test content", written_content)
            self.assertIn("Scraped from", written_content)


class TestConfigLoading(unittest.TestCase):
    """Test configuration loading."""

    def test_load_config_missing_file(self):
        """Test loading config when file doesn't exist."""
        result = scraper.load_config(Path("nonexistent.yaml"))
        self.assertEqual(result, {})

    def test_load_config_json(self):
        """Test loading JSON config."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write('{"rate_limit": 5.0, "timeout": 60}')
            f.flush()
            config_path = Path(f.name)

        try:
            result = scraper.load_config(config_path)
            self.assertEqual(result["rate_limit"], 5.0)
            self.assertEqual(result["timeout"], 60)
        finally:
            config_path.unlink()


class TestMainFunction(unittest.TestCase):
    """Test main CLI function."""

    @patch("crawlforai_scraper.scrape_with_retry")
    @patch("crawlforai_scraper.write_output")
    def test_main_single_url(self, mock_write, mock_scrape):
        """Test scraping a single URL."""
        mock_scrape.return_value = "Scraped content"

        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "output.md"
            result = scraper.main([
                "https://example.com/test",
                "-o", str(output)
            ])

            self.assertEqual(result, 0)
            mock_scrape.assert_called_once()
            mock_write.assert_called_once()

    def test_main_dry_run(self):
        """Test dry-run mode."""
        result = scraper.main([
            "https://example.com/test",
            "--dry-run"
        ])
        self.assertEqual(result, 0)

    @patch("crawlforai_scraper.scrape_with_retry")
    @patch("crawlforai_scraper.write_output")
    def test_main_batch_processing(self, mock_write, mock_scrape):
        """Test batch processing mode."""
        mock_scrape.return_value = "Scraped content"

        with tempfile.TemporaryDirectory() as tmpdir:
            batch_file = Path(tmpdir) / "urls.txt"
            batch_file.write_text(
                "https://example.com/1\nhttps://example.com/2\n",
                encoding="utf-8"
            )

            output_dir = Path(tmpdir) / "output"
            result = scraper.main([
                "--batch", str(batch_file),
                "-o", str(output_dir)
            ])

            self.assertEqual(result, 0)
            self.assertEqual(mock_scrape.call_count, 2)


class TestScrapeWithRetry(unittest.TestCase):
    """Test retry logic."""

    @patch("crawlforai_scraper.try_import_and_scrape")
    @patch("crawlforai_scraper.ContentValidator.validate")
    def test_scrape_success_first_attempt(self, mock_validate, mock_import):
        """Test successful scrape on first attempt."""
        mock_import.return_value = "Scraped content"

        result = scraper.scrape_with_retry("https://example.com", max_retries=3)
        self.assertEqual(result, "Scraped content")
        mock_import.assert_called_once()

    @patch("crawlforai_scraper.try_import_and_scrape")
    @patch("crawlforai_scraper.try_cli_and_scrape")
    @patch("crawlforai_scraper.ContentValidator.validate")
    def test_scrape_fallback_to_cli(self, mock_validate, mock_cli, mock_import):
        """Test fallback from library to CLI."""
        mock_import.return_value = None
        mock_cli.return_value = "Scraped via CLI"

        result = scraper.scrape_with_retry("https://example.com", max_retries=3)
        self.assertEqual(result, "Scraped via CLI")
        mock_import.assert_called_once()
        mock_cli.assert_called_once()

    @patch("crawlforai_scraper.try_import_and_scrape")
    @patch("crawlforai_scraper.try_cli_and_scrape")
    @patch("time.sleep")
    def test_scrape_retry_on_failure(self, mock_sleep, mock_cli, mock_import):
        """Test retry logic on failure."""
        mock_import.return_value = None
        mock_cli.return_value = None

        with self.assertRaises(scraper.ScraperError):
            scraper.scrape_with_retry("https://example.com", max_retries=3)

        # Should try 3 times
        self.assertEqual(mock_import.call_count, 3)


if __name__ == "__main__":
    unittest.main()
