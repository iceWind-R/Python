import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['python123.io'] # 可选
    start_urls = ['http://python123.io/ws/demo.html'] # 待解析的url

    def parse(self, response):
        fname = response.url.split('/')[-1] # 提取文件名
        with open(fname, 'wb') as f: # 写入文件
            f.write(response.body)   # 相应的body，即全部的html代码
        self.log('Save file %s.' % fname)
