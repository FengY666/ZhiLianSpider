# -*- coding: utf-8 -*-
import json
import time
import scrapy
from scrapy.http import Request
import logging

from recruiting_info.data_transfer import dbmongo
from recruiting_info.items import RecruitingInfoItem

all_detail_url = []
class ZhilianWebsiteSpider(scrapy.Spider):
    name = 'zhilian_website'
    # start_urls = ['https://fe-api.zhaopin.com/c/i/sou?start=0&pageSize=60&cityId=801']

    repetition_count = 0
    conn = dbmongo()
    db = conn[1]
    next_page_url ='https://sou.zhaopin.com/?p={page}&jl=801'
    logger = logging.getLogger(__name__)

    def start_requests(self):  #Requests listpage, callback = parse_list
        for page in range(0,3200):
            yield Request(url=self.next_page_url.format(page=page),callback=self.details_request,dont_filter=True,meta={'usedSen':True,'page':page})
            if page == 3199:
                self.logger.info('数据库重复次数:%d' % self.repetition_count)
    # def parse_list(self,response): # parse listpage  Extract detailsurl Requests detailsurls
    #
    #     result = response.xpath('//a[@class="contentpile__content__wrapper__item__info"]/@href').extract()
    #     for detail_url in result:
    #         all_detail_url.append(detail_url)

    def details_request(self,response):
        result = response.xpath('//a[@class="contentpile__content__wrapper__item__info"]/@href').extract()
        for detail_url in result:   #遍历全部详情页url
            # all_detail_url.append(detail_url)
            #详情页请求
            count = self.db['recruiting_info'].find_one({'detail_url':detail_url})
            if count:
                self.repetition_count += 1
                continue
            yield Request(url=detail_url,callback=self.details2_parse,dont_filter=True,meta={'usedSen':False})

    def details2_parse(self,response):   #详情页解析 获取数据
        ip_is_ban = response.xpath('//title/text()').extract_first()
        if ip_is_ban == '智联云NGX-WAF防护':
            self.logger.warning('该网站ip被封,15s后再次请求: %s' % response.url)
            time.sleep(20)
            Request(url=response.url,callback=self.details2_parse,dont_filter=True)
            return
        if 'xiaoyuan' in response.url:
            post_name = response.xpath('//h1[@id="JobName"]/text()').extract_first().replace('\r\n','').replace(' ','')
            job_require = ['工作地点:'+response.xpath('//li[@id="currentJobCity"]/@title').extract_first('未填写'),
                           '经验不限',
                           '学历要求:'+response.xpath('//ul[@class="cJobDetailInforBotWrap clearfix c3"]/li[12]/text()').extract_first('未填写'),
                           '招聘人数:'+response.xpath('//ul[@class="cJobDetailInforBotWrap clearfix c3"]/li[6]/text()').extract_first('未填写')]
            salary = '工资面议'
            company_name = response.xpath('//li[@id="jobCompany"]/a/text()').extract_first('未填写')
            company_case = ['公司行业:'+response.xpath('//ul[@class="cJobDetailInforTopWrap clearfix c3"]/li[4]/@title').extract_first('服务类型未填写'),
                                '公司类型:'+response.xpath('//ul[@class="cJobDetailInforTopWrap clearfix c3"]/li[8]/text()').extract_first('公司性质未填写'),
                                '公司规模:'+response.xpath('//ul[@class="cJobDetailInforTopWrap clearfix c3"]/li[6]/text()').extract_first('公司人数未填写'),
                                '职位类型:'+response.xpath('//ul[@class="cJobDetailInforBotWrap clearfix c3"]/li[4]/text()').extract_first('岗位类型未填写')]

            job_sec = response.xpath('//div[@class="clearfix p20"]/p[@class="c9"]/text()').extract_first('公司地址未填写')
            update_time = response.xpath('//li[@id="liJobPublishDate"]/text()').extract_first('未填写')
            detail_url = response.url
            input_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            info_source = '智联校招'
        else:
            post_name = response.xpath('//h1[@class="l info-h3"]/text()').extract_first()
            job_require = ['工作地点:'+str(response.xpath('//div[@class="info-three l"]/span[1]/a/text()').extract_first('未填写'))+str(response.xpath('//div[@class="info-three l"]/span[1]/text()').extract_first('')),
                           '工作经验:'+response.xpath('//div[@class="info-three l"]/span[2]/text()').extract_first('未填写'),
                           '学历要求:'+response.xpath('//div[@class="info-three l"]/span[3]/text()').extract_first('未填写'),
                           '招聘人数:'+response.xpath('//div[@class="info-three l"]/span[4]/text()').extract_first('未填写')]
            salary = response.xpath('//div[@class="l info-money"]/strong/text()').extract_first()
            company_name = response.xpath('//div[@class="company l"]/a/text()').extract_first()
            company_case = [
                '公司行业:'+response.xpath('//ul[@class="promulgator-ul cl"]/li[1]/strong/a/text()').extract_first('未填写'),
                '公司性质:'+response.xpath('//ul[@class="promulgator-ul cl"]/li[2]/strong/text()').extract_first('未填写'),
                '公司规模:'+response.xpath('//ul[@class="promulgator-ul cl"]/li[3]/strong/text()').extract_first('未填写'),
                '公司网址:'+response.xpath('//ul[@class="promulgator-ul cl"]/li[4]/strong/a/text()').extract_first('未填写')]

            job_sec = response.xpath('//p[@class="add-txt"]/text()').extract_first()
            update_time = response.xpath('//span[@class="company-right"]/span/text()').extract_first()
            detail_url = response.url
            input_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            info_source = '智联社招'

        item = RecruitingInfoItem()

        item['post_name'] = post_name
        item["job_require"] = self.data_dispose(job_require)
        item['salary'] = salary
        item['company_name'] = company_name
        item['company_case'] = company_case
        item['job_sec'] = job_sec
        item['update_time'] = update_time
        item['detail_url'] = detail_url
        item['info_source'] = info_source
        item['input_time'] = input_time
        yield item

    def data_dispose(self,datas):
        if type(datas) == list:
            for i,data in enumerate(datas):
                if data == '\n':
                    del datas[i]
                elif '\n' in data:
                    datas[i] = str(data).replace('\n','')
            return datas

        if type(datas) == str:
            pass