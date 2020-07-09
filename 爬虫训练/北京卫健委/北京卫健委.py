import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def getHTMLText(url):
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url, headers = kv, timeout = 30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text


def parsePageList(html,lst):
    soup = BeautifulSoup(html, 'html.parser')
    info_list = soup.find_all('div', 'weinei_left_con_line_text')
    date_list = soup.find_all('div', 'weinei_left_con_line_date')
    i = 0
    for info in info_list:
        url = info.contents[1].attrs['href']
        if url.startswith('./'):
            url = urljoin('http://wjw.beijing.gov.cn/xwzx_20031/mtjj/', url) # 若为相对地址，则拼接字符串
        content = ''.join(info.contents[1].string.split())
        date = ''.join(date_list[i].string.split())
        lst.append([date, content, url])
        i += 1


def printAndSave(lst, i):
    tplt = "{0:^12}\t{1:{3}^50}\t{2:<50}"
    f = open('北京卫健委.txt', 'a', encoding='utf-8')
    if i == 0:
        print(tplt.format("日期", "标题", "链接", chr(12288)),file=f)

    for info in lst:
        print(tplt.format(info[0], info[1], info[2], chr(12288)),file=f)


def main():
    start_url = 'http://wjw.beijing.gov.cn/xwzx_20031/mtjj/'
    for i in range(21):
        if i == 0:
            url = start_url
        else:
            url = start_url + 'index_'+ str(i) + '.html'
        html = getHTMLText(url)
        info_list = []
        parsePageList(html, info_list)
        printAndSave(info_list, i) # i用来判断是否为第一次，一次打印表头，否则不打印


if __name__ == '__main__':
    main()

