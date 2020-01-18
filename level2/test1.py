# from TemModules import c2f,f2c
# import TemModules
import M1.TemModules as tc

print('32摄氏度= %.2f 华氏度' % tc.c2f(32))
print(tc.f2c(55))

import timeit

print(dir(timeit.__doc__))


