# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Spider_Straitstimes_Item(scrapy.Item):
    #新闻标题
    title=scrapy.Field()
    #新闻正文
    article=scrapy.Field()
    #新闻发布时间
    pubdate=scrapy.Field()
    #新闻作者
    author=scrapy.Field()
    #新闻分类链接
    category_url=scrapy.Field()
    #新闻链接
    news_url=scrapy.Field()
