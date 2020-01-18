# 异常处理
try:
    file_name = input('输入要打开的文件名')
    f= open(file_name)
    for each in f:
        print(each)
except OSError as reason:
    print('文件写错了')
    print('错误原因：' + str(reason))
# 无论如何都会被执行的代码，收尾语句
finally:
    f.close()


# SyntaxError 一般为语法错误
try:
    list = [1,2,3]
    print(list[3])
except Exception as reason:
    print('出错了'+ str(reason))

# //返回整数结果， /返回浮点结果

try:
    int('abc')
except ValueError as reason:
    print('出错了：' + str(reason))
# 用else来表示另一种状态
else:
    print('没有异常')

# try:
#     f = open('test.txt','w')
#     for item in f:
#         print(item)
# except Exception as reason:
#     print('出错了：' + str(reason))
# finally:
#     f.close()

# 用try with 形式，运行完后自动关闭
try:
    with open('test.txt','w') as f:
        for item in f:
            print(item)
except Exception as reason:
    print('出错了：' + str(reason))


