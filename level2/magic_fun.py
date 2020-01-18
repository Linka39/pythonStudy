# 构造和析构
class Rectangle:
    def __init__(self,x,y):
        # self.x为类实例化后 对象的参数
        self.x=x
        self.y=y
    def getPeri(self):
        return (self.x + self.y) *2
    def getArea(self):
        return self.x * self.y

rect = Rectangle(3,4)
print(rect.getArea())

# 继承str
class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls,string)

a = CapStr("I love it")
print(a)

# 析构方法，垃圾回收机制
class C:
    def __init__(self):
        print('init方法被调用了')
    def __del__(self):
        print('del方法被调用了')
# 当引用C()的c1 c2 都被消除后，__del__方法才会被调用
c1=C()
c2 = c1
del c1
del c2

# 利用函数的多态性，对原方法进行重载
class New_int(int):
    # 只有右边是该类的情况时触发
    def __radd__(self, other):
        return int.__sub__(self,other)
    def __sub__(self, other):
        return int.__add__(self,other)
a= New_int('3')
b= New_int(2)
print(a + b)
print(3 + b)








