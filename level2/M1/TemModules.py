def hi():
    print('this is terrible')

def c2f(cel):
    fah = cel *1.8+32
    return fah
def f2c(fah):
    cel = (fah - 32)/1.8
    return cel

# 对当前模块进行测试

def test():
    print('测试0摄氏度=%.2f华氏度' % c2f(0))

# 命名空间为当前模块时
test()
if __name__ == '__main__':
    test()

# 搜索路径设置
import sys

print(sys.path)