# 容器协议，相当于接口
# 不可变的有__len()__,__getItem()
# 可变的要加上setItem(),delItem(),等
class CountList:
    # args,代表数量可变
    def __init__(self,*args):
        self.values = [x for x in args]
        # 初始化字典，对key值进行批量修改
        self.count = {}.fromkeys(range(len(self.values)),0)
    def __len__(self):
        return len(self.values)
    def __getitem__(self, key):
        self.count[key]+=1
        return self.values[key]

c1 = CountList(1,2,3,4)
c2 = CountList(3,5,5,6,9)
print(c1[2])
print(c1[2] + c1[0])
print(c1.count)

# 迭代器 iterator
for i in 'Finish':
    print(i,end='\t')

str1 = 'Finishi'
it = iter(str1)
print(next(it))
print(next(it))
print(next(it))

class Fibs:
    def __init__(self,n=5):
        self.a = 0
        self.b = 1
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.b+self.a
        if self.a > self.n:
            # 发起一个异常
            raise StopIteration
        return self.a

fibs=Fibs()
for each in fibs:
    if each<20:
        print(each)
    else:
        break

# 生成器 可以使调用的函数暂停或挂起，并在需要时让它继续或重新开始
def myGen():
    print('生成器执行！')
    # 相当于return,挂起的意思
    yield 1
    yield 2
mgG = myGen()
for i in myGen():
    print(i)

# not 相当于!
# 生成器推导式
a= [i for i in range(100) if not(i % 2) and i% 3]
print(a)
b={i:i % 2==0 for i in range(10)}
print(b)

