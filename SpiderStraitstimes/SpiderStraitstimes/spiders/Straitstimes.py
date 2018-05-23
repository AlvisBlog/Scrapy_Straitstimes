# -*- coding: utf-8 -*-

import re

import scrapy
from time import sleep
from scrapy import Request
from requests.packages import urllib3
import requests

from SpiderStraitstimes.items import Spider_Straitstimes_Item



class Spider_Straitstimes(scrapy.Spider):
    name = "Straitstimes"
    allowed_domains = ["straitstimes.com"]
    start_urls = ['https://www.straitstimes.com/singapore', 'https://www.straitstimes.com/politics', 'https://www.straitstimes.com/asia', 'https://www.straitstimes.com/world',
                         'https://www.straitstimes.com/videos', 'https://www.straitstimes.com/multimedia', 'https://www.straitstimes.com/lifestyle',
                         'https://www.straitstimes.com/lifestyle/food', 'https://www.straitstimes.com/forum', 'https://www.straitstimes.com/opinion', 'https://www.straitstimes.com/business',
                         'https://www.straitstimes.com/sport', 'https://www.straitstimes.com/tech']



    def parse(self, response):

        html=response.text

        urls = re.findall('<li class=".*?leaf"><a href="(.*?)">', html, re.S)

        for url in urls:

            if 'http' in url:
                pass

            elif 'class' in url:
                pass

            else:
                print("https://www.straitstimes.com"+url)

                item=Spider_Straitstimes_Item()

                item['category_url']="https://www.straitstimes.com"+url


                print("继续访问")

                print(item['category_url'])

                response1 = requests.get(item['category_url'])

                # 获取网页源码
                html = response1.text

                # 提取url
                titles = re.findall('<span class="story-headline">(.*?)</span>' % url, html, re.S)

                for title in titles:

                    item['title']=title.strip()

                    yield item





