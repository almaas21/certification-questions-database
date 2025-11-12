@echo off
REM Helper script for crawlforai scraper operations
REM Usage: scraper.bat [command]

if "%1"=="" goto help
if "%1"=="install" goto install
if "%1"=="test" goto test
if "%1"=="scrape" goto scrape
if "%1"=="batch" goto batch
if "%1"=="clean" goto clean
goto help

:help
echo crawlforai Scraper Helper Script
echo.
echo Usage: scraper.bat [command]
echo.
echo Commands:
echo   install    - Install all dependencies
echo   test       - Run unit tests
echo   scrape     - Scrape a single URL (interactive)
echo   batch      - Process batch file (interactive)
echo   clean      - Clean logs and temporary files
echo.
goto end

:install
echo Installing dependencies...
python -m pip install -r tools\requirements-crawlforai.txt
python -m pip install -r tools\requirements-dev.txt
echo.
echo Installation complete!
goto end

:test
echo Running tests...
python -m pytest tools\test_crawlforai_scraper.py -v --cov=crawlforai_scraper
goto end

:scrape
set /p url="Enter URL to scrape: "
set /p output="Enter output file (default: scraped\output.md): "
if "%output%"=="" set output=scraped\output.md
echo.
echo Scraping %url% to %output%...
python tools\crawlforai_scraper.py "%url%" -o "%output%" -v
goto end

:batch
set /p batchfile="Enter batch file path (default: tools\urls.txt): "
if "%batchfile%"=="" set batchfile=tools\urls.txt
echo.
echo Processing batch file: %batchfile%...
python tools\crawlforai_scraper.py --batch "%batchfile%" -v
goto end

:clean
echo Cleaning logs and temporary files...
if exist tools\scraper.log del tools\scraper.log
if exist scraped\ rmdir /s /q scraped
if exist .pytest_cache\ rmdir /s /q .pytest_cache
if exist __pycache__\ rmdir /s /q __pycache__
if exist tools\__pycache__\ rmdir /s /q tools\__pycache__
echo.
echo Clean complete!
goto end

:end
