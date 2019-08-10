# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

class WikidataPipeline(object):
    def __init__(self):
        self.file1=codecs.open('relation.json','w',encoding="utf-8")
        self.file2=codecs.open('chrmention.json','w',encoding="utf-8")
    def process_item(self, item, spider):
        return item
