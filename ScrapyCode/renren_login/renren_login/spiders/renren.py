import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']


    # 模拟登录，重写该方法(因为在父类中，该方法默认发送GET请求)
    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'
        data = {'email':'13287857692', 'password':'dongao123'}

        # 专门发送POST请求，并且携带表单数据
        request = scrapy.FormRequest(url, formdata = data, callback = self.parse_page)

        yield request

    def parse_page(self, response):
        # with open ('renren.html', 'w', encoding='utf-8') as f:
        #     f.write(response.text)
        # 请求只有登录才能访问的个人主页
        request = scrapy.Request(url='http://www.renren.com/974726184/profile',callback=self.parse_profile)
        yield request

    def parse_profile(self, response):
        with open('myprofile.html', 'w', encoding='utf-8') as f :
            f.write(response.text)
