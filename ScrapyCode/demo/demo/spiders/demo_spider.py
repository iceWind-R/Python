import scrapy


class DemoSpiderSpider(scrapy.Spider):
    name = 'demo_spider'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
