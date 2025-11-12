# crawlforai Scraper - Quick Reference Card

## Installation (One-Time Setup)
```cmd
cd tools
python -m pip install -r requirements-crawlforai.txt
```

## Basic Commands

### Single URL Scrape
```cmd
python crawlforai_scraper.py "URL" -o output.md
```

### With Verbose Logging
```cmd
python crawlforai_scraper.py "URL" -o output.md -v
```

### Dry Run (Test)
```cmd
python crawlforai_scraper.py "URL" --dry-run
```

### Batch Processing
```cmd
python crawlforai_scraper.py --batch urls.txt --rate-limit 5.0
```

### With Configuration
```cmd
python crawlforai_scraper.py --batch urls.txt --config config.yaml
```

## Helper Script (Windows)
```cmd
scraper.bat install    # Install dependencies
scraper.bat scrape     # Interactive single scrape
scraper.bat batch      # Interactive batch processing
scraper.bat test       # Run tests
scraper.bat clean      # Clean logs/temp files
```

## Common Options

| Option | Description | Default |
|--------|-------------|---------|
| `-o, --output` | Output file path | `scraped/examtopics.md` |
| `--rate-limit` | Delay between requests (sec) | `2.0` |
| `--max-retries` | Maximum retry attempts | `3` |
| `--timeout` | Request timeout (sec) | `30` |
| `-v, --verbose` | Enable verbose logging | `False` |
| `--dry-run` | Simulate without scraping | `False` |
| `--prefer-cli` | Prefer CLI over library | `False` |
| `--config` | Config file path | `None` |
| `--batch` | Batch file with URLs | `None` |

## Files

| File | Purpose |
|------|---------|
| `crawlforai_scraper.py` | Main scraper script |
| `test_crawlforai_scraper.py` | Unit tests |
| `requirements-crawlforai.txt` | Production dependencies |
| `requirements-dev.txt` | Development dependencies |
| `config.example.yaml` | Example configuration |
| `urls.example.txt` | Example URL list |
| `scraper.bat` | Windows helper script |
| `scraper.log` | Log file (auto-created) |
| `README-crawlforai.md` | Full documentation |
| `QUICKSTART.md` | 5-minute quick start |
| `PROJECT_SUMMARY.md` | Project overview |

## Typical Workflow

1. **Setup** (one-time)
   ```cmd
   scraper.bat install
   ```

2. **Prepare URLs**
   ```cmd
   copy urls.example.txt urls.txt
   # Edit urls.txt with your URLs
   ```

3. **Test First**
   ```cmd
   python crawlforai_scraper.py --batch urls.txt --dry-run
   ```

4. **Run Production Scrape**
   ```cmd
   python crawlforai_scraper.py --batch urls.txt --rate-limit 5.0 -v
   ```

5. **Check Results**
   ```cmd
   dir scraped
   type tools\scraper.log
   ```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `crawlforai not found` | `pip install crawlforai` |
| `html2text not found` | `pip install html2text` |
| Content too short | Increase `--timeout`, check URL |
| Blocked/CAPTCHA | Increase `--rate-limit` to 10+ |
| Permission error | Run as Administrator |

## Best Practices

✅ Always use `--dry-run` first  
✅ Set rate limit to 5-10 seconds  
✅ Use `-v` for debugging  
✅ Check logs regularly  
✅ Respect robots.txt  
✅ Validate output files  

## Testing

```cmd
# Run all tests
python -m pytest test_crawlforai_scraper.py -v

# With coverage
python -m pytest test_crawlforai_scraper.py --cov
```

## Log Locations

- **Console**: INFO and above
- **File**: `tools\scraper.log` (all levels)

View logs:
```cmd
type tools\scraper.log
```

## Quick Examples

### Example 1: Single ExamTopics Question
```cmd
python crawlforai_scraper.py "https://www.examtopics.com/discussions/comptia/view/123456" -o comptia/security-q1.md -v
```

### Example 2: Batch with Rate Limiting
```cmd
python crawlforai_scraper.py --batch urls.txt --rate-limit 10.0 --max-retries 5 -v
```

### Example 3: Using Configuration
```cmd
python crawlforai_scraper.py --batch urls.txt --config config.yaml
```

## Documentation Links

- **Quick Start**: `QUICKSTART.md` - 5-minute guide
- **Full Docs**: `README-crawlforai.md` - Complete reference
- **Summary**: `PROJECT_SUMMARY.md` - Project overview

## Support

1. Check logs: `type tools\scraper.log`
2. Run verbose: add `-v` flag
3. Test dry-run: add `--dry-run` flag
4. Review error messages

---

**Version**: 2.0.0 (Production Ready)  
**Created**: November 12, 2025  
**Status**: ✅ Tested and Ready
