# Quick Start Guide - crawlforai Scraper

Get up and running in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection

## Step 1: Install Dependencies (2 minutes)

Open Command Prompt in the project root and run:

```cmd
cd tools
python -m pip install -r requirements-crawlforai.txt
```

Expected output:
```
Successfully installed crawlforai html2text pyyaml ...
```

## Step 2: Test the Installation (1 minute)

Run a dry-run test:

```cmd
python crawlforai_scraper.py "https://example.com" --dry-run
```

Expected output:
```
[DRY RUN] Would scrape https://example.com to scraped\examtopics.md
```

## Step 3: Scrape Your First URL (2 minutes)

Replace with your actual examtopics.com URL:

```cmd
python crawlforai_scraper.py "https://www.examtopics.com/discussions/comptia/view/..." -o scraped\question1.md -v
```

Watch the console for:
- ✅ Scrape attempt logs
- ✅ Content validation
- ✅ File saved confirmation

## Step 4: Check the Output

```cmd
type scraped\question1.md
```

You should see:
- Metadata header with source URL
- Scraped timestamp
- Converted markdown content

## Common Use Cases

### Single Question
```cmd
python crawlforai_scraper.py "https://www.examtopics.com/..." -o comptia\security-q1.md
```

### Multiple Questions (Batch)

1. Create `urls.txt`:
```
https://www.examtopics.com/discussions/comptia/view/123
https://www.examtopics.com/discussions/comptia/view/124
https://www.examtopics.com/discussions/comptia/view/125
```

2. Process the batch:
```cmd
python crawlforai_scraper.py --batch urls.txt -o scraped\ --rate-limit 5.0
```

### With Configuration

1. Copy example config:
```cmd
copy config.example.yaml config.yaml
```

2. Edit `config.yaml` with your settings

3. Run with config:
```cmd
python crawlforai_scraper.py --batch urls.txt --config config.yaml
```

## Using the Helper Script

The helper script makes common tasks easier:

```cmd
# Install everything
scraper.bat install

# Interactive single URL scrape
scraper.bat scrape

# Interactive batch processing
scraper.bat batch

# Run tests
scraper.bat test

# Clean up
scraper.bat clean
```

## Troubleshooting

### "crawlforai not found"
```cmd
python -m pip install crawlforai
```

### "Module not found: html2text"
```cmd
python -m pip install html2text
```

### Permission errors
Run Command Prompt as Administrator

### Rate limiting / blocked
Increase the delay:
```cmd
python crawlforai_scraper.py "URL" --rate-limit 10.0
```

## Next Steps

1. **Read the full README** - `tools\README-crawlforai.md`
2. **Set up configuration** - Customize `config.yaml`
3. **Prepare your URLs** - Create a batch file
4. **Run production scrapes** - With proper rate limiting
5. **Review logs** - Check `tools\scraper.log`

## Best Practices

✅ Always use `--dry-run` first  
✅ Set appropriate rate limits (5-10 seconds)  
✅ Check robots.txt before scraping  
✅ Monitor logs for errors  
✅ Validate output files  
✅ Respect site terms of service  

## Getting Help

Check the logs:
```cmd
type tools\scraper.log
```

Run with verbose mode:
```cmd
python crawlforai_scraper.py "URL" -v
```

Test with dry-run:
```cmd
python crawlforai_scraper.py "URL" --dry-run
```

## Summary

You now have a production-ready scraper that:
- ✅ Handles errors gracefully
- ✅ Retries on failures
- ✅ Respects rate limits
- ✅ Converts HTML to markdown
- ✅ Validates content
- ✅ Logs everything
- ✅ Supports batch processing

Happy scraping! 🚀
