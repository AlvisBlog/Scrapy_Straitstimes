# -*- coding: utf-8 -*-
import scrapy
import re
from Spider_Quora.items import Spiderquora_question_Item,Spiderquora_answer_Item
class QuoraSpider(scrapy.Spider):
    name = 'quora'

    def start_requests(self):
        url='https://www.quora.com/What-is-the-greatest-danger-from-political-division'

        scrapy.Request(url=url,callback=self.parse)


    def parse(self, response):

        html=response.text
        print(html)

