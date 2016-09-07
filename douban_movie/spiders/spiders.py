# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from douban_movie.items import DoubanMovieItem
from bson import ObjectId
import logging

logger = logging.getLogger('doubanspider')

class Spiders(CrawlSpider):
    name = "movie"
    start_urls = [
        "https://movie.douban.com/top250/"
    ]



    #def start_requests(self):
        #url = "https://movie.douban.com/top250"
        #yield Request(url=url, callback=self.parse0)

    def parse(self,response):

        selector = Selector(response)
        ol_li = selector.xpath('//div[@class="item"]')

        for li in ol_li:
            movie = DoubanMovieItem()
            movie['_id'] = str(ObjectId())
            movie['rank'] = li.xpath('div[@class="pic"]/em/text()').extract_first()
            movie['link'] = li.xpath('div[@class="pic"]/a/@href').extract_first()
            movie['img'] = li.xpath('div[@class="pic"]/a/img/@src').extract_first()
            movie['title'] = li.xpath('div[@class="pic"]/a/img/@alt').extract_first()
            movie['star'] = li.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract_first()
            movie['quote'] = li.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()').extract_first()
            yield movie

        next_page = response.xpath('//span[@class="next"]/a/@href')
        logger.info("-------------------url %s ",response.url)
        if next_page:
            #logger.info('==============next %s ',next_page)
            #logger.info('=============page %s ',next_page[0].extract())
            #url = response.url.join(next_page[0].extract())
            url = 'https://movie.douban.com/top250'+next_page[0].extract()
            logger.info('=================url %s ',url)
            yield Request(url=url,callback=self.parse)
