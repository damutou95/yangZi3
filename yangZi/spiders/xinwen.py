# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from yangZi import settings
from yangZi.items import YangziItem
class XinwenSpider(scrapy.Spider):
    name = 'xinwen'
    #allowed_domains = ['dafjk']
    headers = settings.HEADERS
    start_urls = 'http://www.yangtse.com/app/jiangsu/nanjing/2018-12-11/650383.html'
    def start_requests(self):
        yield Request(self.start_urls,callback=self.parse,headers=self.headers)
    def parse(self, response):
        item = YangziItem()
        item['title'] = response.xpath('//*[@class="text-title"]/text()').extract_first()
        item['origin'] = response.xpath('//*[@class="text-time"]/text()').extract_first()
        item['content'] = response.xpath('string(//*[@class="text-text"]/p)').extract_first().strip()
        with open('yangziwanbaoxinwen.docx','a') as f:
            f.write(item['title']+'\n'+item['origin']+'\n'+item['content'])
        yield item
