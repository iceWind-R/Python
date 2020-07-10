# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonLinesItemExporter

class VxappPipeline:
    def __init__(self):
        self.fp = open('微信小程序教程.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii = False)


    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.fp.close()