# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderblogItem(scrapy.Item):
    question_title=scrapy.Field()
    question_link=scrapy.Field()
    question_pubAuthor=scrapy.Field()
    question_pubdate=scrapy.Field()
    question_visitorsNum=scrapy.Field()
    question_tag=scrapy.Field()
    question_summary=scrapy.Field()
    question_answeredNum=scrapy.Field()
    question_value=scrapy.Field()
