import scrapy
from urllib.parse import urljoin
from qsbk.items import QsbkItem


class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/text/page/1/']

    def parse(self, response):
        # selectorList 类型
        duanziDivs = response.xpath("//div[@class='col1 old-style-col1']/div")

        i = 0

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

            # tplt = "{0:{2}<20}\t{1:^50}"
            # print(tplt.format(author,url,chr(12288)))
            # print(content)
            # print('=' * 100)

            # duanzi = {'author':author,'content':content} # 即为一个个的存储项，item，写法如下 ⬇
            item = QsbkItem(author=author, content=content)

            i += 1
            print('生成器调用：',i)

            # yield duanzi
            yield item

            # 若不使用生成器，即注释上面的yield item，可使用以下方法
            # items = []
            # items.append(item)
            # return items
            # 返回所有的items=，在pipelines中也可以被解析
        next_path = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get() # 底部显示页面的最后一个li标签，‘下一页’

        if not next_path: # 如果没有下一页
            return
        else:
            next_url = urljoin(self.start_urls[0], next_path)
            yield scrapy.Request(next_url, callback=self.parse) # 利用当前页的url，执行上面的parse解析函数