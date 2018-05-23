# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpiderstraitstimesPipeline(object):
    def process_item(self, item, spider):
        with open("data.text", 'a') as fp:
            fp.write(item['category_url']  +item['title'] + '\n')
