import scrapy
import hashlib

from downrara.items import DownraraItem

fopen = open('../newdownlist.txt','r')
lines = fopen.readlines()

filelistname = "xl.txt"
fo = open(filelistname, 'w')

_urls = []
_names = {}
item = {}
_url_list = {}
item['file_urls'] = []
for r in lines:
    r = r.strip('\n\t')
    r = r.strip('   \t  ')
    if len(r) > 0:
        r = r.split(",")
        # print(r)
        xxx = "https://www.xkb1.com{}".format(r[1])
        _urls.append(xxx)
        _url_hash = hashlib.shake_256(xxx.encode())

        _names[_url_hash] = r[0]
        _url_list[_url_hash] = xxx
        item['file_urls'].append(xxx)
        fo.write(f"{xxx}\n")

print("=====================================",len(_names))



class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = [_urls[0]]
    def parse(self, response):
        for k in _names:
            item = DownraraItem(Title=_names[k],file_urls=[_url_list[k]],url=_url_list[k])
            yield item
        
       

