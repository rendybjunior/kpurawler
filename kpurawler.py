import sys
import time

import scrapy
import json

class DctSpider(scrapy.Spider):
    name = 'dct_crawler'
    dapil_id = '4782' # ID Dapil Cianjur 2
    current_ts = round(time.time() * 1000)
    start_urls = ['https://infopemilu.kpu.go.id/pileg2019/pencalonan/pengajuan-calon/' + \
        str(dapil_id) + '/calonDct.json?_=' + str(current_ts)]

    def parse(self, response):
        rows = json.loads(response.text)
        for row in rows:
            calon_id = row.get('id')
            next_page = "https://silonpemilu.kpu.go.id/publik/calon/" + \
                str(calon_id) + "/2" # 2 denotes 3rd file we download: track record
            yield scrapy.Request(next_page, callback=self.save_pdf)

    def save_pdf(self, response):
        path = response.url.split('/')[-2] + ".pdf"
        if response.status == 200:
            download_size = len(response.body)
            if download_size == 0:
                self.logger.warn('Zero kb response on %s', path)
            else:
                self.logger.info('Saving PDF %s', path)
                with open(path, 'wb') as f:
                    f.write(response.body)
        else:
            self.logger.warn('Not success response %s', response.status)