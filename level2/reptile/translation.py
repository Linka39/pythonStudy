import urllib.request

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
# res =urllib.request.urlopen(url)
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'


data = {}
data['i']= 'Externally added files can be added to Git'
data['from']= 'AUTO'
data['to']= 'AUTO'
data['smartresult']= 'dict'
data['client']= 'fanyideskweb'
data['salt']= '15786449910032'
data['sign']= 'cd3dac93ed6380b6c6b257d15f942213'
data['ts']= '1578644991003'
data['bv']= '3a019e7d0dda4bcd253903675f2209a5'
data['doctype']= 'json'
data['version']= '2.1'
data['keyfrom']= 'fanyi.web'
data['action']='FY_BY_CLICKBUTTION'

# encode为加码，decode解码
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url,data,head)
res = urllib.request.urlopen(req)
html = res.read().decode('utf-8')
print(html)

