print(type("334"))
print(type(44.22))
score = int(input("请输入你的分数："))
# elif = else if
if 100 >= score >= 90:
    print('A')
elif 90 > score >=60:
    print('B')
elif 60 > score >=0:
    print('C')
else:
    print("输入错误！")

# 三元表达式
x,y=4,5
small = x if x < y else y
print(small)
# 断言(assert) 当条件成立后让程序自动崩溃，确保某个条件一定为真

favorite = 'liuly'
for i in favorite:
    print(i, end=' ')

# 列表
print('------------------------')
member = ['白猫','黑猫','大脸猫','蓝皮鼠']
for item in member:
    print(item,len(item),end=' ')

# range()，第三个参数为步进的意思
range(5)
for i in range(5):
    print(i)
for i in range(1,10,2):
    print(i)

bingo = '我自己'
answer = input('说，你喜欢谁：')
while True:
    if answer == bingo:
        break
    answer = input('猜错了，重新说')
print("yes")

for i in range(10):
    if i%2 != 0:
        print(i)
        continue
    i += 2
    print(i)

