# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RecruitingInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    post_name =scrapy.Field()
    job_require = scrapy.Field()
    salary = scrapy.Field()
    company_name = scrapy.Field()
    company_case = scrapy.Field()
    job_sec = scrapy.Field()
    update_time = scrapy.Field()
    info_source = scrapy.Field()
    detail_url = scrapy.Field()
    input_time = scrapy.Field()


