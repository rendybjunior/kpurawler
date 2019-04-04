# kpurawler
Crawl KPU track record data.
Features:
1. Automatically download pdf for all candidate on your Dapil
2. Skip zero bytes pdf file

Ideas? Please submit issues.

## Known issues
1. Does not check whether pdf file is corrupt or not
2. DPD is not supported yet, as the page layout is totally different

# How to use
Note: This is still MVP, so manual works needed
1. Clone this repo
2. Change `dapil_id` value based on your own dapil, see 
3. Run `scrapy runspider kpurawler.py`

## How to find dapil id
The number highlighted by red circle on the url is what we are looking for.
![alt text](https://github.com/rendybjunior/kpurawler/blob/master/dapil_id.jpg?raw=true)
Here's one way that I find works
1. Go to [KPU official site](https://infopemilu.kpu.go.id/)
2. Click `Jenis Pemilihan` on the header
3. Click `Pileg 2019` on the dropdown
4. Click `Daerah Pemilihan` on the header, you'll see a map of Indonesia
5. Choose the option, eg. `DPRD Kabko`, `Jawa Barat`, `Cianjur`, you'll see another pop up on the right side
6. Click your Dapil, and you should be redirected to page illustrated

## Prerequisite to use
1. Scrapy installed. See [How to install Scrapy](http://doc.scrapy.org/en/latest/intro/install.html)
