from distutils import file_util
from os import path
import scrapy
import numpy as np
import pandas as pd
# 'https://www.xkb1.com/yingyu/liunianjishiti/'

_urls = []
i = 1
while i <= 97:
    _urls.append("https://www.xkb1.com/yingyu/wunianjishiti/list_186_{}.html".format(i))
    i+=1

i = 1
while i <= 98:
    _urls.append("https://www.xkb1.com/yingyu/sinianjishiti/list_185_{}.html".format(i))
    i+=1

i = 1
while i <= 98:
    _urls.append("https://www.xkb1.com/yingyu/sannianjishiti/list_184_{}.html".format(i))
    i+=1

i = 1
while i <= 11:
    _urls.append("https://www.xkb1.com/yingyu/xiaoxueernianjiyingyushiti/list_208_{}.html".format(i))
    i+=1
print(_urls)


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = _urls

    filelistname = "filelist.txt"
    fo = open(filelistname, 'w')

    def parse(self, response):
        # _l = response.xpath('yingyu/liunianjishiti').getall()
        # print(_l)
        links = response.xpath('//a[contains(@href, "shiti")]/@href')
        # print(links.getall())
        for index, link in enumerate(links):
            href_xpath = link.get()
            if len(href_xpath.split("/")) == 5:
                print(f'Link number {index} points to url {href_xpath!r}')
                self.fo.write(f"{href_xpath!r}\n")

            

        # links = response.xpath('//a[contains(@href, "list_")]')
        # print(links.getall())

        # urls = []
        
        # for index, link in enumerate(links):
        #     href_xpath = link.xpath('@href').get()
        #     print(f'Link number {index} points to url {href_xpath!r}')
        #     urls.append(f"{href_xpath!r}")

           
           

            # yield Request(link.url, callback=self.parse)
        
        # print(urls)
        # data = np.array(urls)
        # data.tofile('urls')

        # a = pd.DataFrame(data)
        # a.to_csv('urls.csv')
        # _l = response.css('img').xpath('@src').getall()
        # print(_l)
        # _l =response.css('a::attr(href)').getall()
        # print(_l)
        # # /yingyu/liunianjishiti
        # for title in response.('.oxy-post-title'):
        #     yield {'title': title.css('::text').get()}

        # for next_page in response.css('a.next'):
        #     yield response.follow(next_page, self.parse)



def detail(url):
    pass


