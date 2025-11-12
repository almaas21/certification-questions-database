# crawlforai Production-Ready Web Scraper

A robust, production-ready web scraper using `crawlforai` for collecting certification questions from sites like examtopics.com.

## Features

✅ **Robust Error Handling** - Comprehensive logging and error recovery  
✅ **Retry Logic** - Exponential backoff for transient failures  
✅ **Rate Limiting** - Respects target sites with configurable delays  
✅ **HTML to Markdown** - Automatic conversion using html2text  
✅ **Content Validation** - Detects blocked/invalid content  
✅ **Batch Processing** - Process multiple URLs from a file  
✅ **Configuration Files** - YAML/JSON config support  
✅ **Dry-Run Mode** - Test without actually scraping  
✅ **Comprehensive Logging** - File and console logs with rotation  
✅ **Unit Tests** - Full test coverage with pytest

## Installation

### Quick Install

```cmd
cd tools
python -m pip install -r requirements-crawlforai.txt
```

### Dependencies

- `crawlforai` - Core scraping library/CLI
- `html2text` - HTML to Markdown conversion
- `pyyaml` - Configuration file support
- `requests` - HTTP handling (optional)
- `tqdm` - Progress bars (optional)

## Usage

### Single URL Scraping

Basic usage:
```cmd
python tools\crawlforai_scraper.py "https://www.examtopics.com/discussions/..." -o scraped\question1.md
```

With verbose logging:
```cmd
python tools\crawlforai_scraper.py "https://www.examtopics.com/discussions/..." -o scraped\question1.md -v
```

Dry-run (test without scraping):
```cmd
python tools\crawlforai_scraper.py "https://www.examtopics.com/discussions/..." --dry-run
```

### Batch Processing

Create a file with URLs (one per line):
```cmd
# urls.txt
https://www.examtopics.com/discussions/comptia/view/...
https://www.examtopics.com/discussions/amazon/view/...
https://www.examtopics.com/discussions/microsoft/view/...
```

Process the batch:
```cmd
python tools\crawlforai_scraper.py --batch urls.txt -o scraped\
```

### Configuration File

Create `config.yaml`:
```yaml
rate_limit: 2.0
max_retries: 3
timeout: 30
output_dir: "scraped"
convert_html: true
min_content_length: 100
```

Use the config:
```cmd
python tools\crawlforai_scraper.py "https://example.com" --config config.yaml
```

### Advanced Options

```cmd
# Prefer CLI over library
python tools\crawlforai_scraper.py "URL" --prefer-cli

# Custom rate limit (5 seconds between requests)
python tools\crawlforai_scraper.py "URL" --rate-limit 5.0

# Increase retries
python tools\crawlforai_scraper.py "URL" --max-retries 5

# Custom timeout
python tools\crawlforai_scraper.py "URL" --timeout 60
```

## Command-Line Reference

```
usage: crawlforai_scraper.py [-h] [-o OUTPUT] [--prefer-cli] [--config CONFIG]
                             [--batch BATCH] [--rate-limit RATE_LIMIT]
                             [--max-retries MAX_RETRIES] [--timeout TIMEOUT]
                             [--dry-run] [-v] [--convert-html]
                             [url]

Arguments:
  url                    URL to scrape
  -o, --output          Output file path (default: scraped/examtopics.md)
  --prefer-cli          Prefer crawlforai CLI over library
  --config CONFIG       Configuration file (YAML or JSON)
  --batch BATCH         Batch file with URLs (one per line)
  --rate-limit RATE     Minimum delay between requests (default: 2.0)
  --max-retries RETRIES Maximum retry attempts (default: 3)
  --timeout TIMEOUT     Request timeout in seconds (default: 30)
  --dry-run            Simulate without scraping
  -v, --verbose         Enable verbose logging
  --convert-html        Convert HTML to markdown (default: True)
```

## Logging

Logs are written to:
- **Console** - INFO level and above
- **File** - `tools/scraper.log` - All levels with timestamps

View logs:
```cmd
type tools\scraper.log
```

Tail logs (PowerShell):
```powershell
Get-Content tools\scraper.log -Wait -Tail 20
```

## Testing

Run the test suite:
```cmd
python -m pip install pytest pytest-cov
python -m pytest tools\test_crawlforai_scraper.py -v
```

With coverage report:
```cmd
python -m pytest tools\test_crawlforai_scraper.py --cov=crawlforai_scraper --cov-report=html
```

## Production Deployment

### 1. Install Dependencies
```cmd
python -m pip install -r tools\requirements-crawlforai.txt
```

### 2. Configure Settings
Copy and customize:
```cmd
copy tools\config.example.yaml tools\config.yaml
copy tools\urls.example.txt tools\urls.txt
```

Edit `config.yaml` with your rate limits and settings.

### 3. Test with Dry-Run
```cmd
python tools\crawlforai_scraper.py --batch tools\urls.txt --dry-run -v
```

### 4. Run Production Scrape
```cmd
python tools\crawlforai_scraper.py --batch tools\urls.txt --config tools\config.yaml
```

### 5. Schedule Regular Runs (Optional)

Windows Task Scheduler:
```cmd
schtasks /create /tn "Scrape Questions" /tr "python C:\path\to\tools\crawlforai_scraper.py --batch urls.txt" /sc daily /st 02:00
```

## Error Handling

The scraper includes:

- **Validation Errors** - Detects blocked content, CAPTCHAs, rate limits
- **Retry Logic** - Exponential backoff (1s, 2s, 4s, ...)
- **Timeout Protection** - Configurable request timeouts
- **Graceful Failures** - Continues batch processing on individual failures

Common errors and solutions:

| Error | Cause | Solution |
|-------|-------|----------|
| `Content too short` | Empty response | Check URL, increase timeout |
| `blocked or restricted` | CAPTCHA/rate limit | Increase rate-limit delay |
| `crawlforai not found` | Not installed | Run pip install |
| `Timeout` | Slow response | Increase --timeout value |

## Best Practices

### Rate Limiting
- Use `--rate-limit 5.0` or higher for production
- Respect robots.txt and site terms of service
- Avoid peak hours when possible

### Batch Processing
- Process in small batches (10-20 URLs)
- Use `--dry-run` first to validate
- Monitor logs for failures

### Content Validation
- Check output files for completeness
- Verify markdown conversion quality
- Review logs for validation errors

## Legal and Ethical Guidelines

⚠️ **Important**: Before scraping any website:

1. **Check robots.txt** - Respect site crawling rules
2. **Read Terms of Service** - Ensure scraping is permitted
3. **Use Rate Limiting** - Don't overload target servers
4. **Respect Copyright** - Only use scraped content legally
5. **Attribute Sources** - Maintain provenance metadata

The scraper automatically adds metadata headers to scraped content including:
- Source URL
- Scrape timestamp
- Scraper version

## Troubleshooting

### crawlforai not found
```cmd
python -m pip install crawlforai
# Or try: pip install crawlforai
```

### Import errors
```cmd
python -m pip install -r tools\requirements-crawlforai.txt --upgrade
```

### Permission errors
```cmd
# Run as administrator or check folder permissions
icacls scraped /grant %USERNAME%:F
```

### HTML not converting
```cmd
python -m pip install html2text --upgrade
```

## Project Structure

```
tools/
├── crawlforai_scraper.py          # Main scraper script
├── test_crawlforai_scraper.py     # Unit tests
├── requirements-crawlforai.txt    # Python dependencies
├── config.example.yaml            # Example configuration
├── urls.example.txt               # Example URL list
├── scraper.log                    # Log file (auto-created)
└── README-crawlforai.md          # This file

scraped/                           # Default output directory
└── (scraped markdown files)
```

## Contributing

To extend the scraper:

1. **Add new features** in `crawlforai_scraper.py`
2. **Add tests** in `test_crawlforai_scraper.py`
3. **Update docs** in this README
4. **Test thoroughly** with `--dry-run` first

## Support

For issues:
1. Check logs: `type tools\scraper.log`
2. Run with `-v` flag for verbose output
3. Test with `--dry-run` to isolate problems
4. Review error messages and stack traces

## License

See repository root LICENSE file.

## Changelog

### v2.0.0 (Production Ready)
- ✅ Added comprehensive error handling
- ✅ Implemented retry logic with exponential backoff
- ✅ Added rate limiting
- ✅ HTML to Markdown conversion
- ✅ Content validation
- ✅ Configuration file support
- ✅ Batch processing
- ✅ Dry-run mode
- ✅ Full logging system
- ✅ Unit test suite
- ✅ Production deployment guide

### v1.0.0 (Initial)
- Basic crawlforai wrapper
- Simple CLI interface
