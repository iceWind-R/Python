import scrapy
from urllib.parse import urljoin


class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/text/page/1/']

    def parse(self, response):
        # selectorList 类型
        duanziDivs = response.xpath("//div[@class='col1 old-style-col1']/div")
        for div in duanziDivs:
            # div: Selector类型
            # div.xpath()：selectorList类型
            author = div.xpath(".//h2/text()").get().strip()
            # get()函数，取到第一个结果（str类型）, get()<=>extract_first()
            # extract(): 提取所有结果组成列表，每个元素是str类型
            # strip(): 去掉前后的空格

            href = div.xpath('./a/@href').get() # 获取a标签内的href的属性值
            url = urljoin(self.start_urls[0],href) # 跳转到详情页

            content = div.xpath(".//div[@class='content']//text()").extract()
            # html中该div下有span标签，span中才是内容，//text()直接提取该内容

            content = ''.join(content).strip()

            tplt = "{0:{2}<20}\t{1:^50}"
            print(tplt.format(author,url,chr(12288)))
            print(content)
            print('=' * 100)