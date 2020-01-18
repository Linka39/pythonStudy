import urllib.request
import os
import random

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')

    # proxies = ['119.6.144.70:81', '111.1.36.9:80', '203.144.144.162:8080']
    # proxy = random.choice(proxies)
    # proxy_support = urllib.request.ProxyHandler({'http':proxy})
    # opener = urllib.request.build_opener(proxy_support)
    # urllib.request.install_opener(opener)

    res = urllib.request.urlopen(url)
    html = res.read()
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('class-name')+ 23
    # 第一个参数为起始位置，第二个为结束位置
    b = html.find(']',a)
    return html[a:b]

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addr =[]
    a = html.find('img src=')

    while a != -1:
        # 第二个参数为起始位置，第三个为结束位置
        b = html.find('.jpg', a, a + 255)
        if b != -1:
            img_addr.append(html[a+9:b+4])
        else:
            b = a+9
        a = html.find('img src=',b)
    for each in img_addr:
        print(each)
    # 打印出每张图片的地址
    return img_addr

def save_imgs(folder,img_addrs):
    for each in img_addrs:
        # python 中获取倒数第一个数组元素
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)

def download_mm(folder='abc',pages=5):
    os.mkdir(folder)
    os.chdir(folder)
    url = "http://jandan.net/ooxx/"

    for i in range(pages):
        page_url = url + 'MjAyMDAxMTUtMTI' + str(i) + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder,img_addrs)

if __name__ == '__main__':
    download_mm()

