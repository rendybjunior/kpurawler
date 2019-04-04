# kpurawler
Crawl KPU track record data.
Features:
1. Automatically download pdf for all candidate on your Dapil
2. Skip zero bytes pdf file

Ideas? Please submit issues.

## Known issues
1. Does not check whether pdf file is corrupt or not

# How to use
Note: This is still MVP, so manual works needed
1. Clone this repo
2. Change `dapil_id` value
3. Run `scrapy runspider kpurawler.py`

## Prerequisite to use
1. Scrapy installed. See [How to install Scrapy](http://doc.scrapy.org/en/latest/intro/install.html)
