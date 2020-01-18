# 实现永久存储 将元组，列表登数据转换为二进制的形式来存储
# 泡菜
import pickle
my_list = [123,3.14,['you','can']]
# 后缀名为了标识pickle，约定用pkl形式保存, 'wb' 'rb' 为以二进制形式进行写，读操作
pickle_file = open('my_list.pkl','wb')
# 将my_list 倒到 pickle_file 里
pickle.dump(my_list,pickle_file)

pickle_file.close()
# 读取相对路径上的文件
pickle_file = open('my_list.pkl','rb')
# 二进制方式来转换
my_list2 = pickle.load(pickle_file)
print(my_list2)

# pickle_file = open('test.pkl','rb')
# city = pickle.load(pickle_file)
