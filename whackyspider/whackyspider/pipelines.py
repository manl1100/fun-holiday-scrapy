# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class WhackyspiderPipeline(object):
    def process_item(self, item, spider):
        if not item['holiday'] and not item['day']:
            raise DropItem('Missing holiday and day of week')
        else:
            return item
