
import scrapy
import numpy as np
import pandas as pd
import hashlib
from os.path import splitext

# 'https://www.xkb1.com/yingyu/liunianjishiti/'


# 同时使用图片和文件Pipeline
ITEM_PIPELINES={
    'scrapy.pipelines.files.FilesPipeline': 1,
}
# 文件和图片存储路径
FILES_STORE = 'C:/Users/vv/Desktop/yytk/xxx'


fopen = open('newdownlist.txt','r')
lines = fopen.readlines()

filelistname = "xl.txt"
fo = open(filelistname, 'w')

_urls = []
_names = {}
item = {}
item['file_urls'] = []
for r in lines:
    r = r.strip('\n\t')
    r = r.strip('   \t  ')
    if len(r) > 0:
        r = r.split(",")
        # print(r)
        xxx = "https://www.xkb1.com{}".format(r[1])
        _urls.append(xxx)
        _url_hash = hashlib.shake_256(xxx.encode()).hexdigest(5)

        _names[_url_hash] = r[0]
        item['file_urls'].append(xxx)
        fo.write(f"{xxx}\n")


class PytestItem(scrapy.Item):
   Title = scrapy.Field()
   file_urls = scrapy.Field()
   files = scrapy.Field()

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    allowed_domains = ['www.xkb1.com']
    start_urls = _urls
    items = item

    # filelistname = "newdownlist.txt"
    # fo = open(filelistname, 'w')


    def parse(self, response):
        _url_hash = hashlib.shake_256(response.url.encode()).hexdigest(5)

        d_url = response.url
        d_name = _names[_url_hash]
        print(d_url,d_name)

        # with open("xxx/{}.rar".format(d_name),'w') as f:
        #     f.write(response.text)
         

        yield {
            'Tile':"xxx",
            'file_urls':_urls
        }


# class DownloadMusicSpider(scrapy.Spider):
#     # ...
#     def parse(response):
#         item = {}
#         # 提取 url 组装成列表，并赋给 item 的 file_urls 字段
#         for url in response.xpath('//a/@href').extract():
#             download_url = response.urljoin(url)
#             item['file_urls'].append(download_url)
#         yield item
       


from itemadapter import ItemAdapter


class PytestPipeline:
    def process_item(self, item, spider):
        return item
