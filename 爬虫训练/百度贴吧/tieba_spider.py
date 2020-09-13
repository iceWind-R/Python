import requests


class TieBaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}" # {} 为后续用format方法
        self.headers = {"user-agent":"Mozilla/5.0"}

    def get_url_list(self): # 构造Url列表
        # url_list = []
        # for i in range(5):
        #     url_list.append(self.url_temp.format(i * 50))
        # return url_list

        # 简便用法，需要掌握
        return [self.url_temp.format(i * 50) for i in range(5)]

    def parse_url(self, url): # 发送请求，获取相应
        print(url)
        r = requests.get(url, headers=self.headers)
        return r.content.decode()

    def save_html(self, html_str, page_num): # 保存html字符串
        file_path = "{}-第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, "w", encoding="utf-8") as f: # LOL-第3页.html 添加 encoding参数
            f.write(html_str)

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            html_str = self.parse_url(url)
            page_num = url_list.index(url) + 1 # 页码数
            self.save_html(html_str, page_num)

if __name__ == "__main__":
    tiebaSpider = TieBaSpider("李毅")
    tiebaSpider.run()