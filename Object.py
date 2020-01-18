# 类名首字母大写表示，定义一个类，实现后期批量使用
class Turtle:
    # 属性
    color='green'
    legs = 4
    shell = True
    # 类相当于一个模具，实例化是根据模具建造出不同的 对象，它们每个在内存中都有特定的存储位置
    # 方法 , 方法中的self 相当于C++中的this指针，用于区别实例化的不同对象
    def run(self):
        print('跑跑跑')
    def eat(self):
        print('吃东西')

# 若声明时没赋值的话，会被python垃圾回收机制清除
Turtle()
tt= Turtle()
print(tt.color)
# print(tt.pp)
tt.run()

 # 继承
class MyList(list):
    pass

# 多态 ，不同对象对同一方法相应不同的行动
class A:
    def fun(self):
        print('A号选手')

class B:
    def fun(self):
        print('B号选哈哈哈')
a=A()
b=B()
a.fun()
b.fun()

class Ball:
    def setName(self,name):
        self.name = name
    def kick(self):
        print('我叫%s,被踢了' % self.name)

class Ball2:
    # 重写init方法，相当于构造函数
    def __init__(self,name):
        self.name = name
    def kick(self):
        print('我叫%s,被踢了' % self.name)

a= Ball()
a.setName('球A')
a.kick()
# b = Ball()
# b.kick()
b= Ball2('b球')
b.kick()





