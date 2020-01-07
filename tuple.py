# 元组：元组是不可改变，不能排序的
# 用小括号来定义的
tuple1 = (1,2,3,4,5)
print(tuple1[:3])
print(tuple1[1])
tuple2 = tuple1[:]
print(tuple2)
temp = (1)
print(type(temp))
# 小括号并不一定是必须的
temp = 1,3,4,5
print(type(temp))

print(8 * (8))
# 此为元组乘以8
print(8 * (8,))
temp = ('you','are','so','cool')
# 利用切片方式来插入
temp = temp[:2] + ('not',) + temp[2:]
# 当temp被赋予一个新数据时，原来的数据未被指向，会被python垃圾回收机制消除
print(temp)


