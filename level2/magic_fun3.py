# 描述符，将某种特殊类型的类的实例 指派给另一个类的属性
class Mydemo:
    def __get__(self, instance, owner):
        print('getting', self, instance, owner)
    def __set__(self, instance, value):
        print('getting', self, instance, value)
    def __delete__(self, instance):
        print('getting', self, instance)

class Test:
    x = Mydemo()

test = Test()
print(test.x)

class MyProperty:
    def __init__(self,fget=None,fset=None,fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self, instance, owner):
        return  self.fget(instance)
    def __set__(self, instance, value):
        self.fset(instance,value)
    def __del__(self,instance):
        self.fdel(instance)

# class C:
#     def __init__(self):
#         self.x = None
#     def getX(self):

class Celsius:
    def __init__(self,value = 26.9):
        self.value = float(value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = float(value)

class huashidu:
    def __get__(self, instance, owner):
        return instance.cel *1.8 +32
    def __set__(self, instance, value):
        instance.cel = (float(value)-32)/1.8


class Temperature:
    cel = Celsius()
    fah = huashidu()
temp = Temperature()
print(temp.cel,temp.fah)
temp.fah = 89
print(temp.cel)