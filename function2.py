# lambda表达式，匿名函数
# python和java有垃圾回收机制，可用lambda表达式
def ds(x):
    return 2*x+1
# :前为原函数的参数，:后为函数的返回值
g  = lambda x : 2*x+1
print(g(5))

def add(a,b):
    return a+b

# 用完后会被python的垃圾回收机制清除
g = lambda x,y:x+y
print(g(1, 2))

# bif filter,第一个参数为过滤的条件，第二个参数为过滤的对象
filter(None,[1,0,False,True])
print(list(filter(None, [1, 0, False, True])))

def odd(x):
    return x%2
temp = range(10)
show = filter(odd,temp)
print(list(show))

list(filter(lambda x:x%2,range(10)))

# bif map,map(x,a[]) 第一个参数为加工方法，第二个为加工的序列参数
print(list(map(lambda x: x * 2, range(10))))

# 递归
def factorial(n):
    result = n
    for i in range(1,n):
        result *= 1
    return result
result = factorial(5)

# 递归1：调用函数自身，2：有停止的返回条件
def factorial2(n):
    if n==1:
        return 1
    else:
        return n*factorial2(n-1)
result = factorial2(5)
print(result)

# 设置最大递归深度
import sys
sys.setrecursionlimit(101)

def feibonaqi(n):
    if n == 1:
        return 1
    elif n ==2 :
        return 1
    else:
        return feibonaqi(n-1) + feibonaqi(n-2)
result = feibonaqi(7)
print('7年后共有 %d 对兔子出生' % result)

def feibonaqi2(n):
    a,b,c=1,1,1
    if(n==1 or n==2):
        return 1
    else:
        i=3
        while(i<=n):
            c=a+b
            a=b
            b=c
            i+=1
        return c

print(feibonaqi2(7))











