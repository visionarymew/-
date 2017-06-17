# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Job51Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobname = scrapy.Field()
    company = scrapy.Field()
    place = scrapy.Field()
    salary  = scrapy.Field()
    pushtime = scrapy.Field()
    experience = scrapy.Field()
    college = scrapy.Field()
    descrip = scrapy.Field()
    address = scrapy.Field()
    joblink = scrapy.Field()
    people = scrapy.Field()
    companylink = scrapy.Field()