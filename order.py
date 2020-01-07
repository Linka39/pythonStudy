a = list()
b = 'I love liuly'
# 字符串，列表，元组都是序列类型
# 序列化为列表，元组
c = list(b)
print(c)
print(a)
d = tuple(b)
e = str(b)
print(d, e)
# len,max,min为长度，最大，最小数
number1 = [2,52,3,15,6,3,1,66,345]
print(len(number1), max(number1))
print(sum(number1))
print(sorted(number1))
# 枚举 enumrate
print(reversed(number1))
print(list(reversed(number1)))