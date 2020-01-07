# def 表示定义一个函数
# 有返回值的叫函数，无返回值的叫过程
def MyFirstFunction():
    print('第一个python函数')
MyFirstFunction()

def add(v1,v2):
    result= v1+v2
    print(result)
add(3,5)

def add2(v1,v2):
    return v1+v2


print(add2(3, 2))
# 函数根据参数的不同可
def sayHello(name ,word):
    print(name +'**'+word)
sayHello('I','You')
sayHello(name='y',word='n')

# 表示收集参数，将其打包为元组
def test(*params):
    print('参数长度：',len(params))
    print('第2个参数为：',params[1])
test(5,23,2,1)

def back():
    return 2,3,'array'

#

print(back())
# # 形参，实参，局部变量，全局变量
# def discounts(price,rate):
#     # 程序块内的为局部变量
#     final_price=price*rate
#     return final_price
# price = float(input('请输入原价：'))
# rate = float(input('请输入折扣率：'))
# new_price = discounts(price,rate)
# print(new_price)

count = 5
def Myfun():
    # global关键字，声明它为全局变量的count
    global count
    count = 10

print(count)
Myfun()
print(count)

# 内嵌函数，内部函数的声明调用都在外部函数内
def fun1():
    print('fun1()正在被调用')
    def fun2():
        print('fun2()正在被调用')
    fun2()

fun1()


# python和js都是面向对象，函数也是对象
def funX(x):
    # 闭包（closure）内部函数里引用的参数是外部函数传来的
    def funY(y):
        return x*y
    return funY


print(funX(2))
print(funX(2)(3))
