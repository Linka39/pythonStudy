str = 'I\'m a hero'
print(str[:4])
# 字符串可当作数组使用
print(str[4])
# 采用拼接方法插入
str1 = str[:5] + ' bad'+ str[5:]
print(str1)
str2 = 'stronger'
# 首字母大写
print(str2.capitalize())
# casefold()为小写
print(str2.count('r'))
print(str2.endswith('er'))
print(str2.find('t'))
print(str2.join('-'))
# 根据所选字符分割成元组
print(str2.partition('on'))
# 替换和替换次数
print(str2.replace('s', 'b', 3))
str3='I love you very much'
# 根据所选字符，将其切成数组
str4=str3.split(' ')
print(str4)
print(str3.replace('o',''))
print(str3.swapcase())