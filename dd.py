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

def down2(url,name,n):
    # if exists(name):
    #     print('exit down2')
    #     return

    print('down2',name)
    r = requests.get(url)
    with open(name,'wb') as f:
        f.write(r.content)
        
    print('down2 ok')

 
def progressbar(cur, total=100):
    percent = '{:.2%}'.format(cur / total)
    sys.stdout.write('\r')
    # sys.stdout.write("[%-50s] %s" % ('=' * int(math.floor(cur * 50 / total)),percent))
    sys.stdout.write("[%-100s] %s" % ('=' * int(cur), percent))
    sys.stdout.flush()


def schedule(blocknum,blocksize,totalsize):
    """
    blocknum:当前已经下载的块
    blocksize:每次传输的块大小
    totalsize:网页文件总大小
    """
    if totalsize == 0:
        percent = 0
    else:
        percent = blocknum * blocksize / totalsize
    if percent > 1.0:
        percent = 1.0
    percent = percent * 100
    print("download : %.2f%%" %(percent))
    progressbar(percent)



def down(url,name,n=0):

    if exists(name):
        print('exit')
        return

    try:
        urllib.request.urlretrieve(url,name,schedule)       
        print('ok') 
    except Exception as e:
        if(n>=100):
            print('???',n,e)
            if exists(name):
                unlink(name)
                print('unlink') 
            down3(url,name)
            return
        
        n+=1
        if exists(name):
            unlink(name)
            print('unlink') 

        down3(url,name, n)
        sleep(1)
        print('???',name,n,e)
        
# fopen = open('./newdownlist.csv','r')
# lines = fopen.readlines()

# filelistname = "xl.txt"
# fo = open(filelistname, 'w')

# _urls = []
# _names = {}
# item = {}
# _url_list = {}
# item['file_urls'] = []
# for r in lines:
#     r = r.strip('\n\t')
#     r = r.strip('   \t  ')
#     if len(r) > 0:
#         r = r.split(",")
#         # print(r)
#         xxx = "https://www.xkb1.com{}".format(r[1])
#         _urls.append(xxx)
#         _url_hash = hashlib.shake_256(xxx.encode())

#         _names[_url_hash] = r[0]
#         _url_list[_url_hash] = xxx
#         item['file_urls'].append(xxx)
#         fo.write(f"{xxx}\n")
#         print(xxx)
#         down(xxx,f'./xxx/{r[0]}.rar')
       

def down3(url,filename,n=0):
    if exists(filename):
        print('exit down3')
        return

    #设置超时时间
    socket.setdefaulttimeout(10)
    try:
        urllib.request.urlretrieve(url,filename,schedule)
    
    #如果超时
    except socket.timeout:
        count = 1
        while count <= 5:
            try:
                urllib.request.urlretrieve(url,filename,schedule)                                                
                break
            except socket.timeout:
                err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d times'%count
                print(err_info)
                count += 1
        if count > 5:
            print("download job failed!")
    except Exception as e:
        down3(url,filename)



from urllib.request import urlretrieve
import sys
import os

prev_reported_download_percent = None

# 首先定义下载 hook，作为 urllib.request.urlretrive 的关键字参数
def download_hook(count, block_size, total_size):
    """ 接口是写死的 """
    global prev_reported_download_percent
    percent = int(count*block_size*100/total_size)
    if prev_reported_download_percent != percent:
        if percent % 5 == 0:
            sys.stdout.write('%s%%' % percent)
            sys.stdout.flush()
        else:
            sys.stdout.write('.')
            sys.stdout.flush()
        prev_reported_download_percent = percent

def maybe_download(url,filename, force=False):
    """ force 表示是否强制下载 """
    if force or not os.path.exists(filename):
        print('Attempting to download')
        filename, _ = urlretrieve(url, filename, reporthook=download_hook)
            # url+filename：表示文件的 url 地址，
            # filename 则为保存到本地时的文件名
        print('\nDownload completed!')
    # statinfo = os.stat(filename)
    return filename