# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderblogItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link=scrapy.Field()
    title=scrapy.Field()
    author=scrapy.Field()
    pubdate=scrapy.Field()
    read_num =scrapy.Field()
    comment_num=scrapy.Field()