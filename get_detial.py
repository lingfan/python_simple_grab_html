

import scrapy
import numpy as np
import pandas as pd
# 'https://www.xkb1.com/yingyu/liunianjishiti/'

fopen = open('filelist.txt','r')
lines = fopen.readlines()


_urls = []
for r in lines:
    r = r.strip('\n')
    r = r.strip('\'')
    _urls.append("https://www.xkb1.com{}".format(r))



class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = _urls

    

    def parse(self, response):
        print(response.url)
        # _l = response.xpath('yingyu/liunianjishiti').getall()
        # print(_l)
        links = response.xpath('//a[contains(@href, "/plus/download.php")]')
        # print(links.getall())
        for index, link in enumerate(links):
            href_xpath = link.xpath('@href').get()
            print(f'Link number {index} points to url {href_xpath!r}')
            filelistname = "downlist.txt"
            fo = open(filelistname, 'a')

            fo.write(f"{href_xpath!r}\n")
            fo.close()

       


