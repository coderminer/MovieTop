# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from items import DoubanMovieItem

class DoubanMoviePipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost',27017)
        db = client['Movie']
        self.DoubanMovieItem = db['MovieInfo']

    def process_item(self, item, spider):
        if isinstance(item,DoubanMovieItem):
            try:
                self.DoubanMovieItem.insert(dict(item))
            except Exception as e:
                pass
