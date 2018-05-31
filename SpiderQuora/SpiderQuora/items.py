# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Spiderquora_question_Item(scrapy.Item):
    # define the fields for your item here like:
    title=scrapy.Field()
    link=scrapy.Field()
    question_id=scrapy.Field()



class Spiderquora_answer_Item(scrapy.Item):
    # define the fields for your item here like:
    question_id = scrapy.Field()
    answer_content = scrapy.Field()