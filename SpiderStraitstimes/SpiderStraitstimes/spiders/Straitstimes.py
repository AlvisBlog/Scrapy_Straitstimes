# -*- coding: utf-8 -*-

import re
from time import sleep
import time

import scrapy

from scrapy import Request

from SpiderStraitstimes.items import Spider_Straitstimes_Item




class Spider_Straitstimes(scrapy.Spider):
    name = "Straitstimes"

    start_urls=['https://www.straitstimes.com/global']


    '''访问首页'''
    def start_requests(self):

        url='https://www.straitstimes.com/global'

        #接受参数,将首页返回的response返回给parse_parent_category_url函数
        yield Request(url=url,callback=self.parse_parent_category_url)


    '''获取所有的父分类url'''
    def parse_parent_category_url(self,response):

        #获取所有父分类的part_url,状态类似:/test,
        part_parent_urls=re.findall('list-group-item"><a href="(.*?)"',response.text,re.S)

        #遍历所有的父分类url
        for part_parent_url in part_parent_urls:

            #添加完整的域名和主机,形成完整的URL链接
            parent_category_url="https://www.straitstimes.com"+part_parent_url

            #每接受一个父分类URL,即调用一次Request,调用parse_sub_category_url函数
            yield Request(url=parent_category_url,callback=self.parse_sub_category_url)


    '''获取新闻父分类下的子分类的url'''
    def parse_sub_category_url(self, response):

        #request父分类URL获得的网页源代码
        html=response.text

        #提取的部分子分类URL链接,为一个列表
        part_sub_urls = re.findall('<li class=".*?leaf"><a href="(.*?)">', html, re.S)

        #遍历part_sub_urls,获取每一个part_sub_url,类似:/test
        for part_sub_url in part_sub_urls:

            #数据清洗判断
            if 'http' in part_sub_url:

                pass

            #数据清洗判断
            elif 'class' in part_sub_url:

                pass

            else:

                '''翻页操作'''

                for page in range(0,30):

                    #若页数为0则默认访问不带page参数的URL
                    if page==0:

                        url="https://www.straitstimes.com"+part_sub_url

                    #若为其他page数,则携带page参数进行访问
                    else:

                        url="https://www.straitstimes.com"+part_sub_url+"?page=%s"%page

                    print("我是翻页的url:%s"%url)


                    yield Request(url=url,callback=self.parse_news_url)



    '''获取子分类下的新闻链接'''
    def parse_news_url(self,response):

        #获取新闻子分类页面下的part_news_urls,即所有的新闻链接,但是为部分URL
        part_news_urls=re.findall('<span class="story-headline">(.*?)</span>',response.text,re.S)

        #遍历part_news_urls,为新闻链接添加完整的URL
        for part_news_url in part_news_urls:

            #完整的新闻URL
            news_url="https://www.straitstimes.com/"+re.findall('<a href="/(.*?)"',part_news_url,re.S)[0].strip()

            #接受参数,返回至下一个函数parse_news,继续调用该URL
            yield Request(news_url,callback=self.parse_news)


    '''获取新闻的标题,正文,发布时间,作者'''
    def parse_news(self,response):

        #接受访问新闻链接后,返回的news网页源代码
        html=response.text


        #初始化Item
        item=Spider_Straitstimes_Item()


        #获取新闻链接
        try:

            #判断当前的源码是否存在新闻URL
            if len(re.findall('<link rel="canonical" href="(.*?)"',html,re.S))==0:

                #不存在时,默认URL为 no link
                item['link']='no link'

            else:
                #存在则返回具体的link
                item['link']=re.findall('<link rel="canonical" href="(.*?)"',html,re.S)[0]


        #若发生异常时,同样将新闻链接处理为no link,并打印日志
        except Exception as link_error:

            item['link']='no link'

            with open('newsinfo.log','a+') as f:

                f.write(time.strftime("%Y-%m-%d %H:%M:%S")+"新闻链接获取异常:%s"%link_error+"\n")

                f.write("当前新闻链接页面的源码为:%s"%html+"\n")


        # 获取标题信息
        try:

            #判断当前页面是否存在标题信息
            if re.findall('<title>(.*?)</title>', html, re.S)[0]=='':

                #不存在则返回no title
                item['title']='no title'

            else:

                #存在则返回具体的标题
                item['title'] = re.findall('<title>(.*?)</title>', html, re.S)[0]

        # 若发生异常时,同样将标题处理为no title,并打印日志
        except Exception as title_error:

            item['title']="no title"

            with open('newsinfo.log','a+') as f:

                f.write(time.strftime("%Y-%m-%d %H:%M:%S")+"新闻标题获取异常:%s"%title_error+"\n")


        # 获取正文信息
        try:
            #正文被p标签所包围,应先提取正文部分的所有p标签
            data = re.findall('<p>(.*?)</p>', html, re.S)

            #判断是否存在正文
            if len(data) == 0:

                #不存在则返回no article
                item['article'] = 'no article'

            else:
                #存在则遍历提取
                article = ''

                for i in range(1, len(data) - 2):

                    article =article+ data[i].strip()

                item['article']=article

        # 若发生异常时,同样将标题处理为no article,并打印日志
        except Exception as article_error:

            item['article'] = 'no article'

            with open('newsinfo.log','a+') as f:

                f.write(time.strftime("%Y-%m-%d %H:%M:%S")+"新闻正文获取异常:%s"%article_error+"\n")



        # 获取发布时间
        try:
            #判断当前是否可查找发布时间
            if re.findall('"pubdate":"(.*?)",', html, re.S)[0]=='':

                #若不存在则返回no pubdate
                item['pubdate']='no pubdate'

            else:

                #存在则返回具体信息
                item['pubdate'] = re.findall('"pubdate":"(.*?)",', html, re.S)[0]

        # 若发生异常时,同样将标题处理为no pubdate,并打印日志
        except Exception as pubdate_error:

            item['pubdate'] = "no pubdate"

            with open('newsinfo.log','a+') as f:
                f.write(time.strftime("%Y-%m-%d %H:%M:%S")+"新闻发布时间获取异常:%s"%pubdate_error+"\n")



        # 获取作者
        try:
            #判断是否可查找author
            if len(re.findall('"author": "(.*?)",', html, re.S)[0])=='':

                #不存在则返回no author
                item['author'] = "no author"

            else:
                #存在则返回具体信息,并对数据进行预处理
                item['author'] = re.findall('"author": "(.*?)",', html, re.S)[0].replace("+", " ")

        # 若发生异常时,同样将作者处理为no author,并打印日志
        except Exception as author_error:

            item['author'] = "no author"

            with open('newsinfo.log','a+') as f:

                f.write(time.strftime("%Y-%m-%d %H:%M:%S")+"新闻发布者获取异常:%s"%author_error+"\n")



        #判断标题是否涉华
        try:

            if 'china' or 'China' or 'chinese' or 'Chinese' in re.findall('<title>(.*?)</title>', html, re.S)[0] == '':
                # 此时默认标题涉华
                item['title_related_to_China'] = 1
            else:
                # 此时默认标题不涉华
                item['title_related_to_China'] = 0

        # 若发生异常处理
        except Exception as title_related_to_China_error:

            item['title_related_to_China'] = 0

            with open('newsinfo.log', 'a+') as f:

                f.write(time.strftime("%Y-%m-%d %H:%M:%S") + "关系获取异常:%s" % title_related_to_China_error + "\n")



        # 判断内容是否涉华
        try:

            # 正文被p标签所包围,应先提取正文部分的所有p标签
            data = re.findall('<p>(.*?)</p>', html, re.S)

            # 存在则遍历提取
            article = ''

            for i in range(1, len(data) - 2):
                article = article + data[i].strip()


            if 'china' or 'China' or 'chinese' or 'Chinese' in article == '':
                # 此时默认内容涉华
                item['article_related_to_China'] = 1

            else:
                # 此时默认内容不涉华
                item['article_related_to_China'] = 0

        # 若发生异常处理
        except Exception as article_related_to_China_error:

            item['article_related_to_China'] = 0

            with open('newsinfo.log', 'a+') as f:

                f.write(time.strftime("%Y-%m-%d %H:%M:%S") + "关系获取异常:%s" % article_related_to_China_error + "\n")

        #返回item,发送给管道进行数据处理
        yield item







