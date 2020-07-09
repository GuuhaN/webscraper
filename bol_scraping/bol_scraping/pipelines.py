# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonItemExporter
import re

class BolScrapingPipeline:
    def process_item(self, item, spider):
        return item

class ProductCategoryPipeline(object):

    def process_item(self, item, spider):
        if(spider.name != 'productinfo'):
            jsonname = item['base_category'].lower()
            jsonname = re.sub(r"\s+", '-', jsonname)
            self.file = open("categories/" + jsonname + ".json", 'wb')
            self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
            self.exporter.start_exporting()
            self.exporter.export_item(item)
            return item
        else:
            return item


    def close_spider(self, spider):
        if(spider.name != 'productinfo'):
            self.exporter.finish_exporting()
            self.file.close()