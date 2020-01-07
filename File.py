# windows中要带两个反斜杠，因为需要转义
f = open('e:\\readtest.txt')
print(f)
# 获取文件，f.close()关闭文件
print(f.read())
# 已经读到了文件末尾，不能读出来了
print(f.read())
f.close()
f = open('e:\\readtest.txt')
print(f.read(6))
# tell()返回当前文件的所在位置
print(f.tell())