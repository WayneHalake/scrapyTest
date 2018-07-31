# -*- coding: utf-8 -*-

import pymongo
from DoubanGroup.settings import mongo_db_collection,mongo_db_name,mongo_host,mongo_port
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapytestPipeline(object):

    def __init__(self):
        host = mongo_host
        port = mongo_port
        mongoDB = mongo_db_name
        monogColle = mongo_db_collection
        # 创建monogodb 客户
        client = pymongo.MongoClient(host = host, port = port)
        # 创建数据库
        myDB = client[mongoDB]
        # 创建Collection
        self.post = myDB[monogColle]



    def process_item(self, item, spider):
        data =dict(item)
        self.post.insert(data)

        return item
