import requests

r = requests.get("https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png")

with open("a.png", "wb") as f: # 以二进制的方式打开
    f.write(r.content)