# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

class DoubanMovieItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = Field()
    title = Field()
    img = Field()
    rank = Field()
    quote = Field()
    star = Field()
    link = Field()
