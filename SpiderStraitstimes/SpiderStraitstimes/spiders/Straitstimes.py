# -*- coding: utf-8 -*-

import re

import scrapy

from scrapy import Request

from SpiderStraitstimes.items import Spider_Straitstimes_Item



class Spider_Straitstimes(scrapy.Spider):
    name = "Straitstimes"
    allowed_domains = ["straitstimes.com"]
    start_urls = ['https://www.straitstimes.com/singapore', 'https://www.straitstimes.com/politics', 'https://www.straitstimes.com/asia', 'https://www.straitstimes.com/world',
                         'https://www.straitstimes.com/videos', 'https://www.straitstimes.com/multimedia', 'https://www.straitstimes.com/lifestyle',
                         'https://www.straitstimes.com/lifestyle/food', 'https://www.straitstimes.com/forum', 'https://www.straitstimes.com/opinion', 'https://www.straitstimes.com/business',
                         'https://www.straitstimes.com/sport', 'https://www.straitstimes.com/tech']



    '''获取新闻父分类下的子分类的url'''
    def parse(self, response):

        html=response.text

        part_urls = re.findall('<li class=".*?leaf"><a href="(.*?)">', html, re.S)

        for part_url in part_urls:

            if 'http' in part_url:
                pass

            elif 'class' in part_url:
                pass

            else:

                '''包含翻页操作'''

                for page in (1,50):

                    if page==0:

                        url="https://www.straitstimes.com"+part_url

                    else:

                        url="https://www.straitstimes.com"+part_url+"?page=%s"%page

                    print("我是翻页的url%s"%url)

                    yield Request(url,callback=self.parse_news_url)


    '''获取子分类下的新闻链接'''
    def parse_news_url(self,response):


        part_news_urls=re.findall('<span class="story-headline">(.*?)</span>',response.text,re.S)



        for part_news_url in part_news_urls:

            news_url="https://www.straitstimes.com/"+re.findall('<a href="/(.*?)"',part_news_url,re.S)[0].strip()

            print("我要输出新闻链接")

            print(news_url)

            yield Request(news_url,callback=self.parse_news)


    '''获取新闻的标题,正文,发布时间,作者'''
    def parse_news(self,response):


        html=response.text

        item=Spider_Straitstimes_Item()

        # 获取标题信息
        try:
            item['title'] = re.findall('<title>(.*?)</title>', html, re.S)[0]
            if item['title'] == '':
                item['title'] = "no data about title"
        except Exception as e2:
            item['title'] = "no data about title,failed to get it"
        print("标题是:")
        print(item['title'])



        # 获取正文信息
        try:
            data = re.findall('<p>(.*?)</p>', html, re.S)

            if data == []:
                item['article'] = 'no data about article'

            else:
                item['article'] = ''
                for i in range(1, len(data) - 2):
                    item['article'] =item['article'] + data[i]
        except Exception as e1:
            item['article'] = "no data about article,failed to get it"

        print("正文是:")
        print(item['article'])



        # 获取发布时间
        try:
            item['pubdate'] = re.findall('"pubdate":"(.*?)",', html, re.S)[0]
            if  item['pubdate'] == '':
                item['pubdate'] = 'no data about pubdate'
        except Exception as e3:
            item['pubdate'] = "no data about pubdate,failed to get it"
        print("发布时间是")
        print( item['pubdate'])

        # 获取作者
        try:
            item['author'] = re.findall('"author": "(.*?)",', html, re.S)[0].replace("+", " ")
            if item['author'] == "":
                item['author'] = 'no data about author'
        except Exception as e4:
            item['author'] = "no data about author,failed to get it"

        print("作者是")
        print(item['author'])

        yield item







