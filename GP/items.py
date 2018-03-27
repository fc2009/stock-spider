# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GpItem(scrapy.Item):
    # define the fields for your item here like:
    gp_id = scrapy.Field()
    gp_name=scrapy.Field()
    user=scrapy.Field()
    type=scrapy.Field()
    change_num=scrapy.Field()
    end_price=scrapy.Field()
    change_price=scrapy.Field()
    num=scrapy.Field()
    reason_type=scrapy.Field()
    change_date=scrapy.Field()
    gp_type=scrapy.Field()
    relation=scrapy.Field()
    position=scrapy.Field()
