"""
偏函数--functools.partial的作用：把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
"""
print(int('123456'))
print(int('123456', base=8))
print(int('123456', 16))
print(int('101001', 2))


def int2(x, base=2):
    return int(x, base)


print(int2('100000'))
print(int2('101010101'))
'''
functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
'''
import functools

int8 = functools.partial(int, base=8)
print(int8('1234567'))
print(int8('123623541237'))
