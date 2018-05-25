# -*- coding: utf-8 -*-

class SpiderstraitstimesPipeline(object):
    def process_item(self, item, spider):
        with open("news.text", 'a+',encoding='utf-8') as fp:
            fp.write(item['link'] + '\n')
            fp.write(item['title']  + '\n')
            fp.write(item['article'] + '\n')
            fp.write(item['pubdate'] + '\n')
            fp.write(item['author'] + '\n'+ '\n'+ '\n')
