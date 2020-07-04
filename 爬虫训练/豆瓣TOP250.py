# 用于豆瓣2019的TOP250电影爬虫，URL ：https://movie.douban.com/top250
# 输出 排名 电影名 评分
# 存在问题：输出时无法对齐

import requests
import re
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    '''
    解析当前页面的url
    :param url: 待解析的url
    :return: html代码
    '''
    kv = {'user-agent':'Mozilla/5.0'} # 豆瓣有防爬机制，模拟浏览器访问
    r = requests.get(url, headers = kv, timeout = 30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text


def parsePageList(lst, html):
    '''
    解析当前page页的url，保存在列表lst中
    :param url:
    :param page:
    :return:
    '''
    soup = BeautifulSoup(html, 'html.parser')
    li_list = soup.ol.contents # 所有电影内容在ol标签中，ol中的每个电影又包围在li标签，li_list则是所有li组成的列表

    for li in li_list:
        if isinstance(li, bs4.element.Tag): # import bs4 库，使用标签类型
            movie_name = ''
            span_title = li('span','title') # 列表类型，元素即为该电影的名字
            # 第一个li的结果： [<span class="title">蝙蝠侠：黑暗骑士</span>, <span class="title"> / The Dark Knight</span>]

            for span in span_title:
                name = re.sub(r'<.*?>', '', str(span)) # 提取名字字符串。例如： 蝙蝠侠：黑暗骑士
                movie_name += name # 若有多个名字，则合并


            rating_num = li('span','rating_num') # 相应的评分 ,该变量为只有一个元素的列表
            span_rating_num = re.sub(r'<.*?>', '',str(rating_num[0])) # 取出得分
            lst.append([movie_name,span_rating_num])

def printAndSave(lst):
    '''
    保存到文件并打印在控制台
    :param lst:
    :return:
    '''
    i = 0
    tplt = "{:4}\t{:80}\t{:4}"
    print(tplt.format("排名", "电影名", "评分", chr(12288)))
    with open('movie_top250.txt', 'a', encoding='utf-8') as f:
        f.write(tplt.format("排名", "电影名", "评分", chr(12288)))
        f.write('\n')
    for movie in lst:
        i += 1
        print(tplt.format(i, movie[0], movie[1]))
        # print(f'第{i}名：{movie[0]} --- 评分：{movie[1]}')

        # a 模式：如果没文件，则创建，有文件，追加写入
        with open('movie_top250.txt', 'a', encoding='utf-8') as f:
            f.write(tplt.format(i, movie[0], movie[1], chr(12288)))
            f.write('\n')

def main():
    start_url = 'https://movie.douban.com/top250?start='
    info_list = []
    for page in range(10): # 页面依次遍历 0~24 页
        url = start_url + str(25*page)
        html = getHTMLText(url)
        parsePageList(info_list, html)

    printAndSave(info_list)


if __name__ == '__main__':
    main()