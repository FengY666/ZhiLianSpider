# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import logging
from pymongo import MongoClient

from recruiting_info.data_transfer import dbmongo


class MongoPipeline(object):

    # def __init__(self, mongouser, mongopwd,mongoserver,mongoport,mongodbname):
    #     self.mongouser = mongouser
    #     self.mongopwd = mongopwd
    #     self.mongodbname = mongodbname
    #     self.mongoserver = mongoserver
    #     self.mongoport = mongoport
    #
    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(
    #         mongouser=crawler.settings.get('MONGO_URI'),
    #         mongopwd=crawler.settings.get('mongopwd'),
    #         mongoserver = crawler.settings.get('mongoserver'),
    #         mongoport = crawler.settings.get('mongoport'),
    #         mongodbname = crawler.settings.get('mongodbname')
    #     )
    conn = dbmongo()
    client = conn[0]
    db = conn[1]
    insert_count = 0
    update_count = 0

    # def open_spider(self, spider):
        # self.client = pymongo.MongoClient(self.mongo_uri)
        # self.db = self.client[self.mongo_db]
        # uri = 'mongodb://' + self.mongouser + ':' + self.mongopwd + '@' + self.mongoserver + ':' + self.mongoport + '/' + self.mongodbname
        # self.client = MongoClient(uri)
        # self.db = self.client.get_database(self.mongodbname)
        # pass

    def close_spider(self, spider):
        logging.info('本次共插入:%d条数据,更新了:%d数据' %(self.insert_count,self.update_count))
        self.client.close()

    def process_item(self, item, spider):
        count = self.db['recruiting_info'].find_one({'detail_url': item['detail_url']})
        if count:
            self.update_count += 1
            self.db['recruiting_info'].update({'detail_url':item['detail_url']},{'$set':{'update_time':item['update_time']}})
        else:
            self.insert_count += 1
            self.db['recruiting_info'].insert(dict(item))

        # if self.update_count + self.insert_count == 60:
        #     self.insert_count,self.update_count = 0,0
        return item


