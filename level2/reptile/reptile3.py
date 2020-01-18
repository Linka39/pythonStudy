import re
import urllib.request

print(re.search(r'fish', 'i hate fish'))
print(re.search('.', 'me.com'))
print(re.search(r'\.', 'me.com'))
print(re.search(r'\d', 'me 123.com'))
print(re.search(r'[aeiou]', 'I love it'))
print(re.search(r'[2-9]{2}c', '4c,gg332c33c'))
# 正则匹配的是字符串 若[0-255]，则匹配为 0125 中的任一个
# |和c语言中的或一样
print(re.search(r'[0-2][0-9][0-9]', '188'))
print(re.search(r'[01]\d\d|2[0-4]\d|25[0-5]', '188'))

# 小括号代表优先级运算符
print(re.search(r'([01]\d\d|2[0-4]\d|25[0-5]\.){3}[01]\d\d|2[0-4]\d|25[0-5]', '133.002.003.001'))
print(re.findall(r'[a-z]', 'fish'))
print(re.findall(r'[^a-z]', 'sf22'))
# *表示0或多次{0,}，+表示1或多次，?表示0或1次{0,1}
s = "<html>erwerwerwrwer</html>"
print(re.search(r'<.+>', s))
# 此时?表示启用非贪婪模式
print(re.search(r'<.+?>', s))
# 匹配单词分界符，单词包括_
print(re.findall(r'\bg', '2333_g.g!tt_'))

# 通过编译的方式来实现
p=re.compile(r'[A-Z]')
print(type(p))
print(p.findall('i Love It'))

result = re.search(r' (\w+) (\w+)','I llove it')
print(result)

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')
    return html

def get_img(html):
    # ()内为匹配的子组，如果有多个子组时，将会拼接为一个元组形式来展现
    p1=r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.)'
    iplist = re.findall(p1,html)
    p = r'<img class="BDE_Image" src="([^"]+\.jpg")'
    imglist = re.findall(p,html)

    # for each in imglist:
    #     print(each)
    for each in iplist:
        print(each)
    # for each in imglist:
    #     filename = each.split("/")[-1]
    #     urllib.request.urlretrieve(each,filename,None)

if __name__ == '__main__':
    url = 'http://cn.proxy.com'
    get_img(url_open(url))


