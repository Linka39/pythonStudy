f = open('e:\\readtest.txt','w')
f.write('this is imposible?\nhow dare you can love her\n forget it,you\'re never in her heart')
# 写入的文件内容会存在缓冲区里，f.close()后会写入磁盘
f.close()
# windows中要带两个反斜杠，因为需要转义，默认打开为只读模式'r'
f = open('e:\\readtest.txt')
print(f)
# 获取文件，f.close()关闭文件
print(f.read())
# 已经读到了文件末尾，不能读出来了
print(f.read())
f.close()
f = open('e:\\readtest.txt')
print(f.read(6))
# tell()返回当前文件的所在位置，文件由文件指针控制
print(f.tell())
# 45为偏移字节，0表示开始位置
f.seek(3,0)
print(f.readline())

# 按行打印
for each_line in f:
    print(each_line)

f.close()
# 以写入模式打开
f = open('e:\\readtest.txt','w')
f.write('内容重新覆盖')
# 写入的文件内容会存在缓冲区里，f.close()后会写入磁盘
f.close()