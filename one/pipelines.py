# -*- coding: utf-8 -*-
import json
import codecs

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class OnePipeline(object):
    def __init__(self):  
        self.file = codecs.open('one.json', 'wb', encoding='utf-8')
        
    def process_item(self, item, spider):  
        line = json.dumps(dict(item)) + '\n'  

        self.file.write(line.decode("unicode_escape"))  
        return item  
