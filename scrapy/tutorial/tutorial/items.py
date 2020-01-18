# -*- coding: utf-8 -*-

# Define here the models for your scraped items
# 容器文件，保存所需爬取到的数据
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class DmozItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
