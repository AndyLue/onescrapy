# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 一个Item http://wufazhuce.com/
class OneItem(scrapy.Item):
    # define the fields for your item here like:
    vol = scrapy.Field() # 期数
    date = scrapy.Field()
    title = scrapy.Field() # 
    link = scrapy.Field()
    
    article = scrapy.Field()
    article_link = scrapy.Field()
    article_author = scrapy.Field()
    
