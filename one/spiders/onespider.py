# -*- coding: utf-8 -*-

'''
Created on 2014年9月1日

@author: 绝尘
'''
import scrapy
from one.items import OneItem
from scrapy.selector import Selector 

class OneSpider(scrapy.Spider):
    '''
    classdocs
    '''
    name = "one"
    allowed_domains = ["wufazhuce.com"]
    start_urls = [
        "http://wufazhuce.com/"
    ]

    def parse(self, response):
        sel = Selector(response)  
#         items = sel.xpath('//div[@id="carousel-one"]/div[@class="carousel-inner"]/div[@class="item active"]') # 取活跃的（最新的）
        items = sel.xpath('//div[@id="carousel-one"]/div[@class="carousel-inner"]/div')  
#         response.xpath('//a[contains(text(), "悲欢离合")]/text()').extract() // 包含关键字"悲欢离合"
        
        for i in items:
            item = OneItem()
            
            link = i.xpath('a/@href').extract()
            
            # 首页题记，期数
            cita = i.xpath('div[@class="fp-one-cita-wrapper"]')
            vol = cita.xpath('div[@class="fp-one-titulo-pubdate"]/p[@class="titulo"]/text()').extract() # 期数
            title = cita.xpath('div[@class="fp-one-cita"]/a/text()').extract() # 标题
            
            item['link'] = link
            item['vol'] = vol
            item['title'] = [t.encode('utf-8') for t in title if '悲欢离合' in t.encode("utf-8")]  # if
#             for t in title:
#                 print type('悲欢离合')
#                 print type(t.encode("utf-8"))
#                 print t.encode("utf-8")
#                 print '悲欢离合' in t.encode("utf-8")
            
            yield item