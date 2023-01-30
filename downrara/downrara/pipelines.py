# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy import Request
from scrapy.pipelines.files import FilesPipeline

# class DownraraPipeline:
#     def process_item(self, item, spider):
#         return item


class CustomFilePipelines(FilesPipeline):
    def file_path(self, request, response=None, info=None,item=None):
        return '%s.rar' % item['Title']

    def get_media_requests(self, item, info):
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            # "Cookie": "2UuY_2132_saltkey=w69ygI6T; 2UuY_2132_lastvisit=1551345497; Hm_lvt_6ec459bede31ad3361fa26de9edccb1c=1551348959,1551877019; 2UuY_2132_atarget=1; xcount=1; 2UuY_2132_st_t=0%7C1551877342%7C061375cbcb93e3a449b1275bc393bf2d; 2UuY_2132_forum_lastvisit=D_39_1551877292D_40_1551877302D_46_1551877313D_41_1551877342; 2UuY_2132_visitedfid=41D46D40D39; 2UuY_2132_st_p=0%7C1551877531%7C16963e667be50571cf3fcf4c3be73ba0; 2UuY_2132_viewid=tid_212764; Hm_lpvt_6ec459bede31ad3361fa26de9edccb1c=1551878300; security_session_verify=6dae3ecae09b3ff042a6e69b0fb22848; 2UuY_2132_lastact=1551878454%09home.php%09misc; 2UuY_2132_sendmail=1",
            "Host": "www.xkb1.com",
            # "Referer": "{}".format(item["referer"]),
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
        }
        print(item['url'])

        yield Request(url=item['url'],meta={'item':item}, headers=header)


    # def item_completed(self, results, item, info):
    #     return super().item_completed(results, item, info)
