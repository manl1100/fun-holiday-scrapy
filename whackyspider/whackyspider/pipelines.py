# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import calendar
import datetime


class WhackyspiderPipeline(object):
    def process_item(self, item, spider):
        if not item['holiday'] and not item['day']:
            raise DropItem('Missing holiday and day of week')
        else:
            month = str(list(calendar.month_abbr).index(item['date'].split()[0]))
            day = item['date'].split()[1]
            year = str(datetime.datetime.now().year)
            item['date'] = '/'.join([month, day, year])
            return item
