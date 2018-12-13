# -*- coding: utf-8 -*-

# Scrapy settings for recruiting_info project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import datetime

BOT_NAME = 'recruiting_info'

SPIDER_MODULES = ['recruiting_info.spiders']
NEWSPIDER_MODULE = 'recruiting_info.spiders'

to_day = datetime.datetime.now()
log_file_path = 'recruiting_info/log/scrapy_{}_{}_{}.log'.format(to_day.year,to_day.month,to_day.day)

LOG_LEVEL = 'INFO'
LOG_FILE = log_file_path
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'recruiting_info (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.8
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1000000
CONCURRENT_REQUESTS_PER_IP = 0

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS =  {
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.9',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
'Cookie': 'route=eeb200573f6abccac0b821ca3ac31298; sts_deviceid=1676d1e8691573-0ca81a70d8b8df-661f1574-1327104-1676d1e86928a2; adfbid2=0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221676d1e8716748-0a5e62fa2a617d-661f1574-1327104-1676d1e87171ac%22%2C%22%24device_id%22%3A%221676d1e8716748-0a5e62fa2a617d-661f1574-1327104-1676d1e87171ac%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; urlfrom2=121126445; adfcid2=none; ZP_OLD_FLAG=false; campusOperateJobUserInfo=8c93237b-15ca-4120-848e-6ec87523297e; zg_did=%7B%22did%22%3A%20%22167720b915715b-0660838f688224-661f1574-144000-167720b91581f4%22%7D; LastCity=%E6%88%90%E9%83%BD; LastCity%5Fid=801; smidV2=2018120521333622ab0529446ccb919eb140a956c2a9bd0069a300e992bc460; dywez=95841923.1544166939.27.7.dywecsr=fe-api.zhaopin.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/c/i/sou; __utmz=269921210.1544166939.26.7.utmcsr=fe-api.zhaopin.com|utmccn=(referral)|utmcmd=referral|utmcct=/c/i/sou; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1544346245,1544407105,1544503262,1544520292; Hm_lvt_d7ede48beea78a2945672aed33b15da7=1544059945,1544340297,1544347624,1544577333; route=c6b0dccf091c6c7b877b93f631333abd; jobRiskWarning=true; urlfrom=121126445; adfcid=none; adfbid=0; dywea=95841923.4513863443907285500.1543723976.1544520292.1544579103.37; dywec=95841923; sts_sg=1; sts_sid=167a016b804526-0a19bebf071d21-5d1e331c-1327104-167a016b80554f; sts_chnlsid=Unknown; __utma=269921210.1623090428.1543723976.1544520292.1544579103.36; __utmc=269921210; ZL_REPORT_GLOBAL={%22//jobs%22:{%22actionid%22:%221841eaf6-febd-46f6-86c9-53f430b7b4cb-jobs%22%2C%22funczone%22:%22dtl_best_for_you%22}}; sts_evtseq=6; __utmt=1; JSsUserInfo=3D692E6956714071547750755F6A5D7540775D6958695B714C7129772775546ACB24511753693F6925714A7104775B755B6A5D751177586908695871437153770B75586A5D7514775A690F6909714F7156770875586A507544770D690E695D714571547751755B6A00751377286905690A71027111770175476A1575017753692F6926714A7103770C75076A0375097701695A6953714571507729750F6A0B75087705690B6902711B714B770A75066A09754B7729693E695671467157774475586A5675507759695A6951714E715E772875256A5975407753693F692A714A712F772575586A5D75467751695A695E71457155775B75526A3175247755695B6950716; JSpUserInfo=3D692E6956714071547750755F6A5D7540775D6958695B714C7129772775546ACB24511753693F6925714A7104775B755B6A5D751177586908695871437153770B75586A5D7514775A690F6909714F7156770875586A507544770D690E695D714571547751755B6A00751377286905690A71027111770175476A1575017753692F6926714A7103770C75076A0375097701695A6953714571507729750F6A0B75087705690B6902711B714B770A75066A09754B7729693E695671467157774475586A5675507759695A6951714E715E772875256A5975407753693F692A714A712F772575586A5D75467751695A695E71457155775B75526A3175247755695B6950716; at=d03d8618e7a54dcfa574d5da34563741; rt=0beda463781b4fe78f5141736342a4c9; JSShowname=%e5%86%af%e6%80%a1; JSuser1=719690520; MonUid=556443655E6652665D7755754C6F4B754969; CheckedIFL=1; dywem=95841923.y; dyweb=95841923.8.10.1544579103; __utmb=269921210.8.10.1544579103; ASP.NET_SessionId=etrbphkxxs1ssgvele3xixeg; stayTimeCookie=1544580655980; referrerUrl=https%3A//xiaoyuan.zhaopin.com/IndexForLogin; zg_08c5bcee6e9a4c0594a5d34b79b9622a=%7B%22sid%22%3A%201544577333081%2C%22updated%22%3A%201544580661959%2C%22info%22%3A%201544577333084%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22fe-api.zhaopin.com%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%7D; Hm_lpvt_d7ede48beea78a2945672aed33b15da7=1544580662'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'recruiting_info.middlewares.RecruitingInfoSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'recruiting_info.middlewares.RecruitingInfoDownloaderMiddleware': 543,
   'recruiting_info.middlewares.SeleniumMiddleware':543
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# # See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'recruiting_info.pipelines.MongoPipeline': 200,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

SELENIUM_TIMEOUT = 15