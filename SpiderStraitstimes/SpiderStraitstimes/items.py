# -*- coding: utf-8 -*-
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

    #新闻链接
    link=scrapy.Field()