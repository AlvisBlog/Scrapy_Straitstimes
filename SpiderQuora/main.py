# -*- coding: utf-8 -*-


from scrapy import cmdline


def run():
    cmdline.execute('scrapy crawl quora'.split())

run()