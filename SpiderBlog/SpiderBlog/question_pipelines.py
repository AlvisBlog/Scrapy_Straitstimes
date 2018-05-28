# -*- coding: utf-8 -*-

import time

import pymysql

# 用于数据库存储
from SpiderBlog import settings


class DBPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            port=3306,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

        print("数据库连接成功")

    def process_item(self, item, spider):
        try:

            self.cursor.execute("insert into blog_question (question_title,question_link,question_pubAuthor,question_pubdate,question_visitorsnum,question_tag,question_summary,question_answerednum,question_value) "
                            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",[item['question_title'],item['question_link'],item['question_pubAuthor'],item['question_pubdate'],item['question_visitorsNum'],item['question_tag'],item['question_summary'],item['question_answeredNum'],item['question_value']])

            # 提交sql语句
            self.connect.commit()

        except Exception as error:

            with open("db_error.log","a+") as f:

                f.write(time.strftime("%Y-%m-%d %H:%M:%S"+"插入语句执行异常:%s"%error))

