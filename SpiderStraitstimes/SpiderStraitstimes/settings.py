# -*- coding: utf-8 -*-

BOT_NAME = 'SpiderStraitstimes'

SPIDER_MODULES = ['SpiderStraitstimes.spiders']

NEWSPIDER_MODULE = 'SpiderStraitstimes.spiders'

#代理
USER_AGENTS = [
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]


#是否遵循robots协议
ROBOTSTXT_OBEY = False


HTTPERROR_ALLOWED_CODES = [503,403,400]


#访问延迟时间
DOWNLOAD_DELAY = 5

#与DOWNLOAD_DELAY结合使用处理并发情况
CONCURRENT_REQUESTS = 2

#请求的最大数量
CONCURRENT_REQUESTS_PER_DOMAIN = 10

CONCURRENT_REQUESTS_PER_IP = 16

COOKIES_ENABLED = False

TELNETCONSOLE_ENABLED = False

#访问头部
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}


SPIDER_MIDDLEWARES = {
   'SpiderStraitstimes.middlewares.SpiderstraitstimesSpiderMiddleware': 543,
}

#中间件
DOWNLOADER_MIDDLEWARES = {
   'SpiderStraitstimes.middlewares.SpiderstraitstimesDownloaderMiddleware': 543,
}


EXTENSIONS = {
   'scrapy.extensions.telnet.TelnetConsole': None,
}


ITEM_PIPELINES = {
   'SpiderStraitstimes.pipelines.SpiderstraitstimesPipeline': 300,
    'SpiderStraitstimes.dbpipelines.DBPipeline':100
}


AUTOTHROTTLE_ENABLED = True

AUTOTHROTTLE_START_DELAY = 5

AUTOTHROTTLE_MAX_DELAY = 60

AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

AUTOTHROTTLE_DEBUG = False

HTTPCACHE_ENABLED = True

HTTPCACHE_EXPIRATION_SECS = 0

HTTPCACHE_DIR = 'httpcache'

HTTPCACHE_IGNORE_HTTP_CODES = []

HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#Mysql数据库的配置信息
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'straitstimes'         #数据库名字
MYSQL_USER = 'root'                   #数据库账号
MYSQL_PASSWD = ''                     #数据库密码
MYSQL_PORT = 3306                     #数据库端口
FEED_EXPORT_ENCODING = 'utf-8'        #导出文件编码

#IP池
IPPOOL=[
    {"ipaddr":"61.129.70.131:8080"},
    {"ipaddr":"61.152.81.193:9100"},
    {"ipaddr":"120.204.85.29:3128"},
    {"ipaddr":"219.228.126.86:8123"},
    {"ipaddr":"61.152.81.193:9100"},
    {"ipaddr":"218.82.33.225:53853"},
    {"ipaddr":"223.167.190.17:42789"}
]

