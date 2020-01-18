class A():
    def __str__(self):
        return '你喜欢谁'
a= A()
print(a)
class B():
    def __repr__(self):
        return "你喜欢谁"
b=B()
print(b)
# 魔法方法属性访问
class C:
    def __init__(self):
        self.x = 'Xman'

c= C()
c.x=4
print(getattr(c, 'x', '没有这个属性'))

class C:
    def __init__(self,size = 10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self,value):
        self.size=value
    def delSize(self):
        del self.size
    x = property(getSize,setSize,delSize)

c=C()
print(c.x)

# __getattribute__ 要 先于__getattr__ 执行
class C:
    def __getattribute__(self, name):
        print("getattribute")
        return super().__getattribute__(name)
    def __getattr__(self, item):
        print("getattr")
    def __setattr__(self, key, value):
        print("setatr")
        super().__setattr__(key,value)
    def __delattr__(self, item):
        print("delattr")
        super().__delattr__(item)

c = C()
print(c.x)
c.x=3
print(c.x)
del c.x

class rectangle():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __setattr__(self, key, value):
        if key == 'square':
            self.x = value
            self.y = value
        else:
            # self.key = value 调用基类的方法才能避免死循环
            super().__setattr__(key,value)
    def getArea(self):
        return self.x*self.y

a = rectangle()
a.square = 10
print(a.getArea())

