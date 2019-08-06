# clinical-trials-scraper

Author: Deven Kumar

This is a web scraper for clinicaltrials.gov. It was created using the scrapy library in python3. In the folder there are two scrapers, or spiders. The first one, "ctspider," scrapes the page of a specific study to gather information. The other one, "search_spider," scrapes the results off of the results page after a search in clinicaltrials.gov. To use it, write the following command in the terminal:

For ctspider:
```
scrapy crawl clinic -o output-file
```

For search_spider:
```
scrapy crawl search -o output-file
```
"Output-file" must be replaced with your filename. I recommend making your output file a JSON file.
