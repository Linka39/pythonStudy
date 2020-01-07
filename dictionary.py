# 一般方法来映射
brand=['1','2','3','4']
slogan=['one','two','three','four']
print('4的意思是',slogan[brand.index('4')])

# 字典是映射类型，标志位{}花括号,key-value值
dict1 = {'1':'one','2':'two','3':'three','4':'four'}
print('3的意思是:',dict1['3'])
dict2 = {1:'one',3:'three'}
dict2[3]='not three'
# 有的话会更改，没有的话就会自动新增
dict2[4]='four'
print('3的意思是:',dict2[3])

# 字典的内嵌方法，
dict3 = {}
# 获取对应的key值，或进行批量修改
print(dict3.fromkeys((1, 2, 3)))
print(dict3.fromkeys((1, 2, 3),'number'))
dict3 = dict3.fromkeys(range(4),'赞')
print(dict3)
for Key in dict3.keys():
    print(Key)
for Value in dict3.values():
    print(Value)
for Item in dict3.items():
    print(Item)

print(dict3[3],dict3.get(3))

# 当数据规模较大时，判断存在用in , not in 较好一些
print(31 not in dict3, 31 in dict3)

# a,b都是指向数据的指针
a={'name':'liuly'}
b=a
# a={}为重新指向一个空字典，b还是不为空
print(b)
a.clear() # 为清除数据字典
print(b)

a={'1':'one','2':'two','3':'three'}
# 为b开辟一个新的数据空间和地址，并赋值
b=a.copy()
# 字典里的编排并没有顺序
print(a.pop('2'))
print(a.popitem())
# 存入键值
a.setdefault('四','four')
print(a)


