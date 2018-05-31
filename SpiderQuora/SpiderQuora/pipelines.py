# -*- coding: utf-8 -*-

import time

import pymysql

# 用于数据库存储
from SpiderStraitstimes import settings


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

            self.cursor.execute("insert into straitstimes_news (title,link,question_id) "
                                "values(%s,%s,%s)",[ item['title'],item['link'],item['question_id']])

            # 提交sql语句
            self.connect.commit()

        except Exception as error:

            with open("db_error.log","a+") as f:

                f.write(time.strftime("%Y-%m-%d %H:%M:%S"+"插入语句执行异常:%s"%error))

        return item