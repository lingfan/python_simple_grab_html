from genericpath import exists
from os import unlink
from time import sleep
import requests
import scrapy
import numpy as np
import pandas as pd
import hashlib
from os.path import splitext

import socket
import sys

import urllib.request
import numpy as np
import pandas as pd
from dddd import Downloader

# fopen = open('./newdownlist.txt','r',encoding='utf-8')
# lines = fopen.readlines()
df = pd.read_csv('./newdownlist.txt',names=["title","url"])

lines = dict(zip(df['title'],df['url']))

filelistname = "x2.txt"
fo = open(filelistname, 'w',encoding='utf-8')

_urls = []
_names = {}
item = {}
_url_list = {}
item['file_urls'] = []
for r in lines:
    

    r = r.strip('\n\t')
    r = r.strip('   \t  ')
    if len(r) > 0:
        title = r
        url = lines[r]
        # print(r)
        xxx = "https://www.xkb1.com{}".format(url)
        _urls.append(xxx)
        _url_hash = hashlib.shake_256(xxx.encode())

        _names[_url_hash] = title
        _url_list[_url_hash] = xxx
        item['file_urls'].append(xxx)
        fo.write(f"{title},{xxx}\n")
        print(xxx)
        downloader = Downloader(xxx,f"xxx/{title}.rar")
        downloader.start()
       