class Turtle:
    def __init__(self,x):
        self.num = x

class Fish:
    def __init__(self,x):
        self.num = x

class Pool:
    def __init__(self,x,y):
        # 加上self改变的是实例对象的值
        self.turtle = Turtle(x)
        self.fish = Fish(y)
    def print_num(self):
        print('水池里有%d只乌龟，%d只鱼' % (self.turtle.num, self.fish.num))

pool = Pool(1,10)
pool.print_num()

class BB:
    def printBB(self):
        print('no zuo no die')

# class BB2:
#     # 必须加上self参数才能数据绑定到实例化的对象上
#     def printBB():
#         print('no zuo no die')
#
# bb = BB()
# bb.printBB()
# BB2.printBB()
# bb2 = BB2()
# bb2.printBB()

# 类相关的BIF
class A:
    pass
class B(A):
    pass
class C:
    pass

# 判断A 是不是 B 的基类
print(issubclass(B, A))
print(issubclass(B, B))
# object 为所有类的基类
print(issubclass(B, object))
print(issubclass(A, B))

# 第一个参数为object,第二个为class类或类的元组
# isinstance(object,classInfo)
b1 = B()
print(isinstance(b1, B))
print(isinstance(b1, A))
print(isinstance(b1, C))
print(isinstance(b1, (A, B,C)))

class C:
    def __init__(self,x=0):
        self.x = x

c1 = C()
# 判断是否包含属性值，属性值加上''
print(hasattr(c1, 'x'))
# 获取指定属性值，若无此属性值，第三个参数为报错信息
print(getattr(c1, 'x','此属性值不存在'))
print(getattr(c1, 'y', '此属性值不存在'))
# 更改属性值
setattr(c1,'y','存在了')
print(getattr(c1, 'y', '此属性值不存在'))
# 删除属性
delattr(c1,'y')

class C:
    def __init__(self,size = 0):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self,value):
        self.size =value
    def delSize(self):
        del self.size
    # property 3个参数以此为 获取方法，设置方法，删除方法
    # 优势是封装性，用户只要通过x这个属性接口就能调用方法，维护性高
    x = property(getSize,setSize,delSize)

c1 = C()
print(c1.getSize())
print(c1.x)
c1.x=10
print(c1.x)

