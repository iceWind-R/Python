import requests
import sys
import json

query_string = sys.argv[1] # 接受用户输入的参数

headers = {"user-agent":"Mozilla/5.0"}
post_data = {
    "query":query_string,
    "from":"zh",
    "to":"en"
}
post_url = "https://fanyi.baidu.com/basetrans"

r = requests.post(post_url, data=post_data, headers=headers)
dict_ret = json.load(r.content.decode())
ret = dict_ret["trans"][0]["dst"]
print("result is :", ret)