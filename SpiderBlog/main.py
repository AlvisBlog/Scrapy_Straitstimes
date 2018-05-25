# -*- coding: utf-8 -*-

from scrapy import cmdline


def run():
    cmdline.execute('scrapy crawl blog'.split())

run()