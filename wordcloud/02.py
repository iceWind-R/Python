import requests
import re
import jieba
import wordcloud

headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

url='https://api.bilibili.com/x/v1/dm/list.so?oid=217464776'

def get_damu(url):
    response = requests.get(url,headers=headers)
    response = response.content.decode('utf-8')
    data = re.compile('<d.*?>(.*?)</d>')
    damu = data.findall(response)
    danmu_word = jieba.lcut(" ".join(damu))
    print(danmu_word)
    w = wordcloud.WordCloud(font_path='msyh.ttc')
    w.generate(danmu_word)
    w.tofile('danmu.png')

get_damu(url)