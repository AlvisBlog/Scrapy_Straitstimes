# -*- coding: utf-8 -*-

import requests
import re
from requests.packages import urllib3

all_urls=['https://www.quora.com/What-is-the-safest-country-to-visit-right-now-in-the-world']

news_url=[]


def GetUrl(html):

    related_questions=re.findall("""<span class='ui_story_title  '><span class="ui_qtext_rendered_qtext">(.*?)<""",html,re.S)

    for related_question in related_questions:

        url="https://www.quora.com/%s"%related_question.replace(" ","-").strip("?")

        all_urls.append(url)


def remove_url(url):
    all_urls.pop(url)


def start_request():

    for i in range(0,200):

        print("第%s次进行访问"%i)

        try:
            response=requests.get(all_urls[i])

            html=response.text

            GetUrl(html)
        except Exception as error:
            with open("error.log","a+") as f:
                f.write("第%s次访问出错,原因:%s"%(i,error)+"\n")
                continue


def readfile():
    with open("data.text","r") as f:
        for line in f:
            print(line)
            news_url.append(line.strip("\n"))
        print("news_url的起始数据长度:")
        print(len(news_url))


def remove_data():
    print("我开始去重")
    for url in all_urls:
        print(url)
        if not url in news_url:
            news_url.append(url)


def write_data():
    print("重新写入数据")
    for url in news_url:
        try:
            with open("question_url.text","a") as f:
                f.write(url)
                f.write("\n")
        except Exception as e:
            pass

#函数里面调用函数获取消息链接的函数
start_request()

#去重函数,news_url为不重复的消息链接
remove_data()

#重新写入数据
write_data()
