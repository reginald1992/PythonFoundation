"""
偏函数--functools.partial的作用：把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
"""
import functools

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

int8 = functools.partial(int, base=8)
print(int8('1234567'))
print(int8('123623541237'))
'''
注意到上面的这个int8函数，仅仅是把base的默认值设定成了8，但是在调用函数时候还是可以传入别的数值
'''
print(int8('121212356', base=16))
'''
最后，创建偏函数时，实际上可以接收函数对象、*args、**kw这三个参数，当传入int6 = functools.partial(int, base=6),
实际上固定了int（）函数的关键字base，也就是：
'''
int6 = functools.partial(int, base=6)
# 相当于
kw = {'base': 2}
int('121212356', **kw)

# 当传入
max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边
max2(5, 6, 7)
# 相当于
args = (10, 5, 6, 7)
max(*args)

