# -*- coding: utf-8 -*-

from scrapy import signals


import random


#增加动态IP代理类和动态用户代理类
PROXIES = [
    {'ip_port': '106.39.179.244:80'},
    {'ip_port': '65.52.223.99:80'},
    {'ip_port': '1.52.248.207:3128'},
    {'ip_port': '45.77.198.207:3128'},
    {'ip_port': '177.125.119.16:8080'},
    {'ip_port': '174.138.65.233:3128'}
]

class SpiderstraitstimesSpiderMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        pass

    def process_start_requests(self, start_requests, spider):
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SpiderstraitstimesDownloaderMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)





class RandomUserAgent(object):

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        print ("**************************" + random.choice(self.agents))
        request.headers.setdefault('User-Agent', random.choice(self.agents))


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        print("**************ProxyMiddleware no pass************" + proxy['ip_port'])
        request.meta['proxy'] = "http://%s" % proxy['ip_port']
