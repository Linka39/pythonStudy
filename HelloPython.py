import random
print("\'刘凌云,我喜欢你(❤ ω ❤)\'\n"*4)
print(5*100+20)
print('--------------')
secret = random.randint(1,10)
# input()为内置函数
temp = input('猜猜我心里想的哪个数字?')
time = 3
guess = int(temp)
while guess != secret and time>0:
    if guess == secret:
        print('猜对了')
        print('你赢了')
    else:
        if guess < secret:
            print("猜错了，小了，还有"+str(time)+"次机会")
            time -= 1
        if guess > secret:
            print("大了，还有"+str(time)+"次机会")
            time -= 1
        temp = input('猜猜我心里想的哪个数字?')
        guess = int(temp)
if guess != secret:
    print("一败涂地……")
print("GameOver")

# BIF == Built in functions
# /等于小数点除法，//等于整数除法
# **为幂运算 -3**2=-9 (-3)**2= 9
# 优先级，幂运算，正负号，算法操作符，比较操作符，逻辑操作符(and,or,not)
# and==&& or==|| not==!
