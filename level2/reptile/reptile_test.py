import urllib.request
res = urllib.request.urlopen("https://www.baidu.com/s?ie=UTF-8&wd=python%20%E9%AD%94%E6%B3%95")
# 获取的为二进制的数据
html = res.read()
# 编码方式设为utf-8
html = html.decode("utf-8")
# print(html)

