
import urllib.error
import urllib.request
req = urllib.request.Request("http://www.ssssfd.com")
try:
    urllib.request.urlopen(req)
except urllib.error.URLError as e:
    print(e.reason)

req = urllib.request.Request("http://tieba.baidu.com/p/6138204024")
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read())