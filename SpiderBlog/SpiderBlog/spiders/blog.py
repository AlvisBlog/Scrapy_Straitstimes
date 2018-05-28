# -*- coding: utf-8 -*-
import scrapy

from scrapy import Request
import re
from SpiderBlog.items import SpiderblogItem

class BlogSpider(scrapy.Spider):
    name = 'blog'
    #allowed_domains = ['cnblogs.com']
    start_urls = ['https://q.cnblogs.com/tag/list']



    def start_requests(self):


        for page in range(1,101):

            url='https://q.cnblogs.com/tag/list'

            yield Request(url=url,callback=self.parse_tag)


    def parse_tag(self, response):

        category_links=re.findall('<td.*?<li><a href="(.*?)"',response.text,re.S)


        for category_link in category_links:

            for page in range(1,101):

                yield Request(url="https://q.cnblogs.com"+category_link+"?page=%s"%page,callback=self.parse_category_question_list)


    def parse_category_question_list(self,response):

        item=SpiderblogItem()

        question_titles=re.findall('<div id="news_item.*?target="_blank".*?>(.*?)<',response.text,re.S)

        question_links=re.findall('<h2 class="news_entry">.*?href="(.*?)"',response.text,re.S)

        question_pubAuthor=re.findall('news_contributor">(.*?)<',response.text,re.S)

        question_pubdate=re.findall('news_contributor">.*?<span title="(.*?)"',response.text,re.S)

        question_visitorsNum=re.findall('news_contributor.*?<br />(.*?)<span',response.text,re.S)

        question_tags=re.findall('question-tag-div">(.*?)</div>',response.text,re.S)

        question_summarys=re.findall('news_summary">(.*?)</div>',response.text,re.S)

        question_answeredNums=re.findall('diggnum .*?answered">(.*?)<',response.text,re.S)

        question_values=re.findall('<h2 class="news_entry">(.*?)</h2>',response.text,re.S)



        for i in range(len(question_titles)):

            item['question_title']=question_titles[i]
            item['question_link']="https://q.cnblogs.com"+question_links[i]
            item['question_pubAuthor']=question_pubAuthor[i]
            item['question_pubdate']=question_pubdate[i]
            item['question_visitorsNum']=question_visitorsNum[i].strip().strip("浏览(").strip(")")
            item['question_tag']=str(re.findall('<a style=".*?>(.*?)<',question_tags[i].strip(),re.S)).strip("[").strip("]").replace("'","")
            item['question_summary']=question_summarys[i].strip()
            item['question_answeredNum']=question_answeredNums[i]

            data=re.findall('<span class="gold">(.*?)<',question_values[i],re.S)
            if len(data)==0:
                item['question_value']="0"
            else:
                item['question_value']=data[0]

            yield item






