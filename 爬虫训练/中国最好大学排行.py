# CrawUnivRankingA.py
import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30) # r返回的是一个Response对象
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text # 返回的r中的内容，即html代码的字符串形式
    except:
        print('连接失败')
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        # soup.find('tbody')返回的是bs4.element.Tag类型
        # soup.find('tbody').children返回的是list_iterator类型
        if isinstance(tr, bs4.element.Tag): # import bs4 库，使用标签类型
            tds = tr('td') # 简写形式，等价于 tr.find_all('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])


def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))


def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)  # 20 univs


main()