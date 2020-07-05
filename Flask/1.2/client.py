import urllib.request

url = 'http://127.0.0.1:5000'

data = urllib.request.urlopen(url)
html = data.read().decode()
print(html)