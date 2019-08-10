# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WikidataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rid=scrapy.Field()
    rtype=scrapy.Field()
    rsubtype=scrapy.Field()
    rmention=scrapy.Field()
    chrmention=scrapy.Field()
    link=scrapy.Field()

