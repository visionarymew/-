# -*- coding: utf-8 -*-
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
from job51.items import Job51Item

import re
import scrapy
import time

class linkspider(CrawlSpider):
    name = 'job'
    start_urls = ['http://search.51job.com/list/020000,000000,0000,00,9,99,Python,2,1.html']
    rules = (Rule(LinkExtractor(allow=r'welfare=',restrict_xpaths=r"//div[@class='p_in']"),callback='joblist',follow=True),)

    def joblist(self,response):
        #nextlink = response.css('li[class=bk]').extract()[-1]
        jobs = response.xpath("//div[@id='resultList']/div")
        for job in jobs:
            try:
                item = Job51Item()
                item['jobname'] = job.xpath('./p[@class="t1 "]//a/@title').extract()[0]
                item['joblink'] = job.xpath('./p[@class="t1 "]//a/@href').extract()[0]
                item['company'] = job.xpath('./span[@class="t2"]//a/@title').extract()[0]
                item['place'] = job.xpath('./span[@class="t3"]/text()').extract()[0]
                try:
                    item['salary'] = job.xpath('./span[@class="t4"]/text()').extract()[0]
                except:
                    item['salary'] = '面谈'

                yield scrapy.Request(item['joblink'],callback=self.jobinfo,meta={'item':item})
            except:
                print('joblist error',response.url)


    def jobinfo(self,response):
        item = response.meta['item']
        try:
            jobinfo = response.xpath('//div[@class="tCompany_main"]')
            sampleinfo = jobinfo.xpath('.//span[@class="sp4"]')
            for si in sampleinfo:
                type = si.xpath('.//em/@class').extract()[0]
                text = si.xpath('text()').extract()[0]
                tags ={'i1':'experience','i2':'college','i3':'people','i4':'pushtime'}
                item[tags[type]]=text
            item['address'] = jobinfo.xpath('//p[@class="fp"]/text()').extract()[-1].strip()
            item['companylink'] = response.xpath('//p[@class="cname"]/a/@href').extract()[0]
            descrip = jobinfo.xpath('.//div[@class="bmsg job_msg inbox"]/text()').extract()
            clear = [i.replace('\xa0','').strip() for i in descrip]
            clear = [i for i in clear if i != '']
            item['descrip'] = clear
        except:
            pass

        return item
