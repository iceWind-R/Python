import scrapy


class IndexSpider(scrapy.Spider):
    name = 'index'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/iceWind-R']

    def parse(self, response):
        result = response.xpath("//ol[@class='d-flex flex-wrap list-style-none gutter-condensed mb-4 js-pinned-items-reorder-list']/li//p[contains(@class,'pinned-item-des')]/text()").extract()

        print(''.join(result))

