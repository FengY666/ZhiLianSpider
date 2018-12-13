# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger

from scrapy import signals


class RecruitingInfoSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RecruitingInfoDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class SeleniumMiddleware(object):
   def __init__(self, timeout=None):
       self.logger = getLogger(__name__)
       self.timeout = timeout
       self.chrome_opt = webdriver.ChromeOptions()
       self.prefs = {'profile.managed_default_content_settings.images': 2}
       self.chrome_opt.add_experimental_option('prefs', self.prefs)
       self.browser = webdriver.Chrome(chrome_options=self.chrome_opt)
       self.browser.set_window_size(1200, 700)
       self.browser.set_page_load_timeout(self.timeout)
       self.wait = WebDriverWait(self.browser, self.timeout)

   # def __del__(self):
   #     self.browser.close()

   def process_request(self, request, spider):
       """
       用PhantomJS抓取页面
       :param request: Request对象
       :param spider: Spider对象
       :return: HtmlResponse
       """
       self.logger.debug('PhantomJS is Starting')
       Isphantom = request.meta.get('usedSen')
       if Isphantom:
           try:
                self.browser.get(request.url)
                # target = self.browser.find_elements_by_id('homeAlertMask')
                # self.browser.execute_script("arguments[0].scrollIntoView();",target)
                time.sleep(1.5)
                #页面滑动到下面,具体滑动多少,可以修改scrollTop
                js = "var q=document.documentElement.scrollTop=8500"
                self.browser.execute_script(js)
                #等待下一页可点击
                # self.wait.until(
                #     EC.element_to_be_clickable((By.CSS_SELECTOR, '#pagination_content > div > button:nth-child(7)')))
                time.sleep(1.5)
                # self.logger.info(self.browser.page_source)
                text = self.browser.page_source
                #最后一页请求过后关闭webdrive
                if request.meta.get('page') == 3199:
                    self.browser.quit()
                return HtmlResponse(url=request.url, body=text, request=request, encoding='utf-8', status=200)
           except TimeoutException:
                return HtmlResponse(url=request.url, status=500, request=request)

   @classmethod
   def from_crawler(cls, crawler):
       return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'))
