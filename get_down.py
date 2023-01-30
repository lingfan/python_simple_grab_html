

import scrapy
import numpy as np
import pandas as pd
import urllib.parse
# 'https://www.xkb1.com/yingyu/liunianjishiti/'

fopen = open('downlist.txt','r')
lines = fopen.readlines()
fopen.close()

_urls = []
for r in lines:
    r = r.strip('\n')
    r = r.strip('\'')
    _urls.append("https://www.xkb1.com{}".format(r))



class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = _urls

    

    def parse(self, response):
        data = urllib.parse.parse_qs(response.url)
        aid = data['aid'][0]
        
        
        txt = response.xpath("//a[@style='font-size:11pt']/text()")
        _txt = txt.get().strip('    ')
        _txt = _txt.strip('\n\t')
        _txt = _txt.strip('   \t  ')

        # print(txt.get().strip('\n').strip(' '))
        # for i in response.css('.main_articletitle'):
        #     for x in i.xpath('//a[contains(@href, "/plus/download.php")]'):
        #         print("-------------",x.get())
        
        # _l = response.xpath('yingyu/liunianjishiti').getall()
        # print(_l)
        links = response.xpath(f'//a[contains(@href, "/plus/download.php?open=2&id={aid}")]/@href')
        # for l in links:
        #     print(l.get())

        href_xpath1 = links[0].get()
        href_xpath1 = href_xpath1.strip('\n')
        href_xpath1 = href_xpath1.strip('\t')
        href_xpath1 = href_xpath1.strip(' ')

        _txt = _txt.replace('\n','')
        _txt = _txt.replace(' ','')
        _txt = _txt.replace('   	  ','')
        _txt = _txt.replace('\t','')
        _txt = _txt.replace(',','_')


        print(f' {_txt},{href_xpath1}')
        filelistname = "newdownlist.txt"
        fo = open(filelistname, 'a')
        fo.write(f"{_txt},{href_xpath1}")
        fo.close()

       


