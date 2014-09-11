# -*- coding: utf-8 -*-

# Scrapy settings for one project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'one'

SPIDER_MODULES = ['one.spiders']
NEWSPIDER_MODULE = 'one.spiders'

ITEM_PIPELINES = {  
    'one.pipelines.OnePipeline':300  
}  
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'one (+http://www.yourdomain.com)'

# 发送邮件
MAIL_FROM = '123@123'
MAIL_HOST = '123'
MAIL_PORT = '123'
MAIL_USER = '123'
MAIL_PASS = '123'
MAIL_TLS = False
MAIL_SSL = True