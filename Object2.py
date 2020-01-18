# 访问修饰符
class Person:
    # 默认为公有
    name = '乌龟'
    # 加下划线后为私有
    __age = 14
    def getAge(self):
        return self.__age
p = Person()
print(p.name)
# print(p.__age)
# print(p._Person__name)
print(p.getAge())

# 继承
class Parent:
    def hello(self):
        print('正在调用父类方法……')

class Child(Parent):
    def hello(self):
        print('调用子类的方法中')
c= Child()
c.hello()

import random as r

class Fish:
    # 构造函数初始化变量
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print("我的位置是：", self.x, self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass
class Shark(Fish):
    # # 子类重写方法后，相当于把父类的方法覆盖了
    # def __init__(self):
    #     self.hungry = True
    def __init__(self):
        # Fish.__init__(self)  # 实际上实例化的是Shark的self
        super().__init__()  # 用super()方法自动继承之前的父类
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('饿了，要吃东西了')
        else:
            print('吃饱了')

fish1 = Goldfish()
fish1.move()
shark1 = Shark()
shark1.move()
