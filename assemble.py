# 集合 set
num = {}
print(type(num))
# 集合为花括号，没有映射，里面所有的元素都是唯一的，索引上不可映射
num = {1,2,3,4,5,5}
print(type(num),num)

# bif 工厂函数
set1 = set({1,2,3,4,4,5})
num1 = [1,3,32,2,2,2,5]
temp = []
for each in num1:
    if each not in temp:
        temp.append(each)
print(temp)
temp = list(set(num1))
print(temp)

# 冻结集合不可改变里面的值
num2 = frozenset([1,2,34,5])
num2.add(0)
num2.remove(0)