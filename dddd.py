from genericpath import exists
import sys
import requests
import os
 
 
class Downloader(object):
    def __init__(self, url, file_path):
        self.url = url
        self.file_path = file_path
 
    def start(self):
        # if exists(self.file_path):
        #     return

        try:
            res_length = requests.get(self.url, stream=True)
        except Exception as e:
            print('???',e)
            return
        
        total_size = int(res_length.headers['Content-Length'])
        print(res_length.headers)
        print(res_length)
        if os.path.exists(self.file_path):
            temp_size = os.path.getsize(self.file_path)
            print("%s 当前：%d 字节， 总：%d 字节， 已下载：%2.2f%% " % (self.file_path , temp_size, total_size, 100 * temp_size / total_size))
        else:
            temp_size = 0
            print("%s 总：%d 字节，开始下载..." % (self.file_path ,total_size,))
 
        headers = {'Range': 'bytes=%d-' % temp_size,
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"}
        try:
            res_left = requests.get(self.url, stream=True, headers=headers)
        except Exception as e:
            print('???',e)
            self.start()
            return

        with open(self.file_path, "ab") as f:
            for chunk in res_left.iter_content(chunk_size=1024):
                temp_size += len(chunk)
                f.write(chunk)
                f.flush()
 
                done = int(50 * temp_size / total_size)
                sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * temp_size / total_size))
                sys.stdout.flush()

        if temp_size < total_size:
            self.start()
 
