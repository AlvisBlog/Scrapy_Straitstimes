# -*- coding: utf-8 -*-

import requests
import re
import time
all_question_url=[]
with open("question_url.text","r",encoding='gbk') as f:
    for url in f:
        all_question_url.append(url.strip("\n"))

for question_url in all_question_url:
    with open("question_info.text","a",encoding='UTF-8') as f:
        f.write("问题链接为:%s"%question_url+"\n")
    print("问题链接为:%s"%question_url)

    try:
        res=requests.get(question_url)
        time.sleep(3)
        try:
            html = res.text
            try:
                # 提取标题
                title = re.findall('document.title="(.*?)- Quora', html, re.S)[0]
                with open("question_info.text", "a", encoding='UTF-8') as f:
                    f.write("讨论问题是:%s" % title+"\n")
                print("讨论问题是:%s" % title)
                try:
                    # 提取回答
                    all_answers = re.findall('"ui_qtext_rendered_qtext"><p class="ui_qtext_para">(.*?)</span>', html,re.S)
                    # 回答详情,清洗数据
                    for data in all_answers:
                        answer = data.replace("<b>", "").replace("</b>", "").replace('<p class="ui_qtext_para">',"").replace('</p>', "").replace('<span class="qlink_container">',"")
                        with open("question_info.text", "a", encoding='UTF-8') as f:
                            f.write("回答是:%s" % answer+"\n")
                        print("回答是:%s" % answer)
                except Exception as e3:
                    with open("content.text", "a+") as f:
                        f.write(time.strftime("%Y-%m-%d %H:%M:%S") + e3)
            except Exception as e2:
                with open("content.text", "a+") as f:
                    f.write(time.strftime("%Y-%m-%d %H:%M:%S") + e2)
        except Exception as e1:
            with open("content.text", "a+") as f:
                f.write(time.strftime("%Y-%m-%d %H:%M:%S") + e1)
    except Exception as e:
        with open("content.text", "a+") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S") + e)
            continue


