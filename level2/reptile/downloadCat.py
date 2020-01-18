import urllib.request

# req = urllib.request.Request('http://placekitten.com/400/300')
# res = urllib.request.urlopen(req)
res = urllib.request.urlopen('http://placekitten.com/400/300')
print(res.info())
print(res.geturl())
print(res.getcode())
print(type(res))
cat_img = res.read()

with open('cat_500.jpg','wb') as f:
    f.write(cat_img)

