# from itemadapter import ItemAdapter
# import json
#
#
# class QsbkPipeline:
#     def __init__(self):
#         self.fp = open('duanzi.json', 'w', encoding='utf-8')
#
#     # 爬虫启动时执行的函数，比如打开文件，也可写在构造函数中
#     def open_spider(self, spider):
#         print('--------> 爬虫开始了... <---------')
#
#     # 爬虫运行时，即qsbk_spider.py 中的生成器依次调用, item就是yield依次传来的值
#     def process_item(self, item, spider):
#         # item_json = json.dumps(item,ensure_ascii=False) # 第一次，未指定item
#         item_json = json.dumps(dict(item),ensure_ascii=False) # 第二次，指定items.py中的类，此处用dict()函数将其转换为字典
#         self.fp.write(item_json + '\n')
#
#         print('pipelines调用')
#
#         return item
#
#     # 爬虫结束时执行的函数，关闭文件
#     def close_spider(self, spider):
#         self.fp.close()
#         print('--------> 爬虫结束了... <---------')

#######################################################################################################################

# from scrapy.exporters import JsonItemExporter # scrapy框架里的JSON导出器
#
#
# class QsbkPipeline:
#     def __init__(self):
#         self.fp = open('duanzi.json', 'wb') # 二进制方法打开 , 不能指定 encoding = 'utf-8'
#         self.exporter = JsonItemExporter(self.fp, ensure_ascii = False, encoding = 'utf-8')
#         self.exporter.start_exporting() # 开始
#
#     def open_spider(self, spider):
#         print('--------> 爬虫开始了... <---------')
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         print('pipelines调用')
#
#         return item
#
#     def close_spider(self, spider):
#         self.exporter.finish_exporting() # 该方法是把所有的item存为一个列表，每个元素是一个item
#         self.fp.close()
#         print('--------> 爬虫结束了... <---------')

#######################################################################################################################

from scrapy.exporters import JsonLinesItemExporter # scrapy框架里的JSON导出器


class QsbkPipeline:
    def __init__(self):
        self.fp = open('duanzi.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii = False, encoding = 'utf-8')

    def open_spider(self, spider):
        print('--------> 爬虫开始了... <---------')

    def process_item(self, item, spider):
        self.exporter.export_item(item) # 此方法把每个item作为一个单独的字典类型存入文件。
        print('pipelines调用')

        return item

    def close_spider(self, spider):
        self.fp.close()
        print('--------> 爬虫结束了... <---------')