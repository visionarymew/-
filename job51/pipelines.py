# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import json
import pymongo




class jobPipeline(object):
    def __init__(self):
        self.host = settings['MONGODB_HOST']
        self.port = settings['MONGODB_PORT']
        self.dbname = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=self.host, port=self.port)
        mgdb = client[self.dbname]
        self.post = mgdb[settings['MONGODB_DOCNAME']]

    def open_spider(self,spider):
        self.f = open('d:/study/result.txt','w')

    def process_item(self, item, spider):
        #保存到txt
        #self.f.write(str(item)+',\n')
        #保存到JSON
        #info = json.dumps(dict(item),ensure_ascii=False)
        #self.f.write(info+',\n')
        #保存到MONGODB
        info = dict(item)
        self.post.insert(info)

        return item

    def close_spider(self,spider):
        self.f.close()

