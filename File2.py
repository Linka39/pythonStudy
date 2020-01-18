def save_file(boy,girl,count):
    # 新建文件名
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'

    # 以可读方式打开文件
    boy_file = open(file_name_boy, 'w')
    girl_file = open(file_name_girl, 'w')
    boy_file.writelines(boy)
    girl_file.writelines(girl)
    boy_file.close()
    girl_file.close()

f = open('record.txt')
boy = []
girl = []
count = 1
for each_line in f:
    if each_line[:6] != '=======':
        # 元组变量 split(':',1)以冒号来分割一次
        (role, line_spoken) = each_line.split(':', 1)
        if role == '小甲鱼':
            boy.append(line_spoken)
        elif role == '小客服':
            girl.append(line_spoken)
    else:
        save_file(boy,girl,count)
        boy = []
        girl = []
        count += 1
f.close()

# 模块引入 os-operating system，每个os的文件操作系统都不相同，此模块可使python实现跨平台访问文件系统，
import os

print(os.name)
print(os.getcwd())
os.removedirs('e:\\A\\B')
print(os.listdir('e:\\'))
# os.mkdir('e:\\A\\B')
os.makedirs('e:\\A\\B')

# os.system('cmd')  # 打开命令行界面
# 打印当前平台使用的终止符
print(os.linesep)
print(os.path.basename('e:\\a\\b\\test.txt'))
print(os.path.dirname('e:\\a\\b\\test.txt'))
print(os.path.join('C:\\', 'a', 'b', 'c'))
# 返回路径 和 文件名
print(os.path.split('e:\\a\\b\\test.txt'))
print(os.path.getsize('e:\\readtest.txt'))

# 返回此文件的最近访问时间
print(os.path.getatime('e:\\readtest.txt'))
import time
print(time.localtime(os.path.getatime('e:\\readtest.txt'))) # 返回此文件的创建时间
os.path.getatime('e:\\readtest.txt')    # 返回此文件的最近修改时间
print(os.path.isabs('e:\\readtest.txt'))
print(os.path.isfile('e:\\readtest.txt'))

# 判断其是否是个挂载点
print(os.path.ismount('e:\\'))
print(os.path.ismount('e:\\readtest.txt'))









