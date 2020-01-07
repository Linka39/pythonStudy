member = ['you','are','so','cool']
mix = ['I\'m',13,44.22,442,[3,22.3,'john']]
for item in mix:
    print(item,end=" @ ")

mix.append('假面骑士')
print(mix)
print(len(mix))
# append只能添加一个参数，extend可以添加多个参数
# extend 只能添加数组
mix.extend(['超级','钢铁侠'])
print(mix)

# 插入
mix.insert(1,'牡丹花')
mix.insert(0,'zero1')
print(mix)

# 删除
mix.remove('zero1')
del member[0]
print(member)
del member
print(mix)

# pop
name =mix.pop()
print(name)
mix.pop(0)
print(mix)

# 分片
print(mix[1:3])
print(mix[:5])
# 分片完成数组的复制
mix2 = mix[:]

# 列表比较,从列表的第一个元素起开始比较
list1 = [123,3]
list2 = [234,455,1]
print(list1<list2)
# 类似于extend方法
list3 = list1 + list2
print(list3 * 2)
list3*=3
print('我' in list3)
print(3 in list3)

# list内置函数
dir(list)
print(list3.count)
# 看123在列表中出现了多少次
print(list3.count(123))
# 123第一次出现的位置
print(list3.index(123))
list3.reverse()
print(list3)
# sort算法中利用了归并排序，其中并未给list4
list4 = list3.sort()
print(list3)
# reverse= 为sort()中的内置参数
list3.sort(reverse=True)
print(list3)

# 小坑
list2 = list3
# 当中list2只是复制的list3的地址，当list3发生改变，list2也会改变
list2 = list3[:]
# 为数组重新开辟空间来复制


