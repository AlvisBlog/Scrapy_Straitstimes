# -*- coding: utf-8 -*-
import scrapy

from scrapy import Request
import re
from SpiderBlog.items import SpiderblogItem

class BlogSpider(scrapy.Spider):
    name = 'blog'
    #allowed_domains = ['cnblogs.com']
    start_urls = ['http://www.cnblogs.com/']

    def parse(self, response):
        html=response.text

        data=re.findall('<ul id="cate_item">(.*?)</ul>',html,re.S)[0]

        urls=re.findall('<a href="(.*?)"',data,re.S)

        names=re.findall('/">(.*?)</a>',data,re.S)

        for i in range(len(urls)):

            #分类名称
            category_url=self.start_urls[0]+urls[i]

            #分类URL
            category_name=names[i]

            print(category_url)

            yield Request(url=category_url,callback=self.parse_category)


    def parse_category(self,response):


        html=response.text

        article_links=re.findall('<a class="titlelnk" href="(.*?)"',html,re.S)

        article_titles=re.findall('<a class="titlelnk".*?">(.*?)<',html,re.S)

        article_summarys = re.findall('<p class="post_item_summary">.*?</a>(.*?)</p>', html, re.S)

        article_authors=re.findall('class="lightblue">(.*?)<',html,re.S)

        article_pubdates=re.findall('class="lightblue">.*?发布于(.*?)<span',html,re.S)

        article_read_nums=re.findall('l" class="gray">(.*?)<',html,re.S)

        article_comment_nums=re.findall('<span class="article_comment">.*?class="gray">(.*?)</a>',html,re.S)


        item=SpiderblogItem()

        for article_link in article_links:
            item['link']=article_link

        for article_title in article_titles:
            item['title'] = article_title

        # for article_summary in article_summarys:
        #     print(article_summary)

        for article_author in article_authors:
            item['author'] = article_author

        for article_pubdate in article_pubdates:
            item['pubdate'] = article_pubdate

        for article_read_num in article_read_nums:
            item['read_num'] =article_read_num.strip(")").replace('阅读(',"").strip()
        #
        for article_comment_num in article_comment_nums:
            item['comment_num']=article_comment_num.strip(")").replace('评论(',"").strip()

            yield item





