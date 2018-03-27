# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from GP.items import GpItem

class GpSpider(scrapy.Spider):
    name = 'gp'
    allowed_domains = ['sina.com.cn']

    def start_requests(self):
        for i in range(1000):
            base_url='http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/nbjy/index.phtml?num=60&p={}'
            yield Request(base_url.format(str(i+1)))

    def parse(self, response):
        item=GpItem()
        rsps=response.xpath('//div[@id="divContainer"]//tr')
        if rsps :
            for node in rsps:
                item['gp_id']=node.xpath('./td[1]/a/text()').extract_first()
                item['gp_name']=node.xpath('./td[2]/a/text()').extract_first()
                item['user']=node.xpath('./td[3]/text()').extract_first()
                item['type']=node.xpath('./td[4]//text()').extract_first()
                item['change_num']=node.xpath('./td[5]//text()').extract_first()
                item['end_price']=node.xpath('./td[6]/text()').extract_first()
                item['change_price']=node.xpath('./td[7]/text()').extract_first()
                item['num']=node.xpath('./td[8]/text()').extract_first()
                item['reason_type']=node.xpath('./td[9]/text()').extract_first()
                item['change_date']=node.xpath('./td[10]/text()').extract_first()
                item['gp_type']=node.xpath('./td[11]/text()').extract_first()
                item['relation']=node.xpath('./td[12]/text()').extract_first()
                item['position']=node.xpath('./td[13]/text()').extract_first()
                yield item
        else:
            return