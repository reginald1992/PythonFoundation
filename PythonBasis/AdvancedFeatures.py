"""
在Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。
高级特性之一：切片（slice）
"""
# 取一个list或tuple的部分元素是常见的操作，例如：
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
[L[0], L[1], L[2]]  # 最笨的办法
# 用循环解决
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
# 对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
L[0: 3]  # L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
L[: 3]   # 索引从0开始的，还可以这样省略
L[-3: -2]  # 倒数切片
print(L[-3:-2])
L2 = list(range(100))
L2[: 10]  # 前10个数
L2[-10:]  # 后10个数
L2[:10:2]  # 前10个数， 每2个取一个
L2[:]  # 什么都不写，只写[:]就可以复制一个list
(0, 1, 2, 3, 4, 5, 6, 7)[0: 3]  # tuple也是一种list，唯一区别是tuple不可变。tuple也可以用切片操作，操作结果仍是tuple：
'QWWEERRTTYTYYUUUU'[: 5]  # 字符串'xxx'也可以看成是一种list，每个元素是一个字符。字符串也可以用切片操作，结果仍是字符串
print('QWHFJSDFSJDFKSDJF'[::2])

# 练习
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：


def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
"""
TODO 高级特性之二：迭代（iteration）
如果给定一个list或tuple，可以通过for循环遍历这个list或tuple,在Python中迭代是通过for循环完成的，而很多的语言是通过下标完成的
"""
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

# 使用for循环时，只要对象是可迭代的，for循环就能正常运行。如何判定对象是可迭代的？
from collections import Iterable
print(isinstance('abc', Iterable))  # str是否可以迭代
print(isinstance('[a,b,c]', Iterable))  # list是否可以迭代
print(isinstance(123456, Iterable))  # 数字是否可以迭代

# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C', 'D', 'E']):
    print(i, value)

# 在Python中同时引用两个变量
for x, y in[(1, 2), ('A', 'B'), (25, 36)]:
    print(x, y)

# 练习
# 使用迭代在一个list中找到最大值和最小值，并返回一个tuple


def find_min_max(l):
    if len(l) < 1:
        return None, None
    else:
        temp_min = temp_max = l[0]
        for element in l:
            if element > temp_max:
                temp_max = element
            if element < temp_min:
                temp_min = element
        return temp_min, temp_max
# 测试


if find_min_max([]) != (None, None):
    print('测试失败!')
elif find_min_max([7]) != (7, 7):
    print('测试失败!')
elif find_min_max([7, 1]) != (1, 7):
    print('测试失败!')
elif find_min_max([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
"""
TODO 高级特性之三 列表生成器 List Comprehension
生成list【1，2……，10】
"""
list(range(1, 11))
# 生成1*1,2*2，……9*9
print([x*x for x in range(1, 10)])
# 加上判断，筛选出仅偶数的平方
print([x*x for x in range(1, 10) if x % 2 == 0])
# 利用2个循环，生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])
# 列出当前目录下的所有文件名和目录名
import os  # 导入OS模块
print([d for d in os.listdir('.')])  # os.listdir可以列出目录和文件
# for循环同时使用两个甚至多个变量，比如dict()和items()可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + ':' + v for v, k in d.items()])
d_new = {value: key for key, value in d.items()}
print(d, d_new)
# 将一个list中的大写字母变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
"""
练习
如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
使用内建的isinstance函数可以判断一个变量是不是字符串：
>>> x = 'abc'
>>> y = 123
>>> isinstance(x, str)
True
>>> isinstance(y, str)
False
请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
"""
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
"""
高级特性之四：生成器 generator
如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
"""
L = [x * x for x in range(10)]
g = (x * x for x in range(10))
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# next()函数获得generator的下一个返回值
for n in g:
    print(n)
# 用generator生成斐波拉契数列：第三个数开始，任意一个数可以又前2个数相加得到


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return 'done'


fib(8)
# fib函数实际上是定义了斐波拉契数列的推算规则，从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
# 也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        a, b = b, a+b
        n = n + 1
    return 'done'


# 这就是定义generator的另一种方法。
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
f = fib(8)
# generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
# 请注意区分普通函数和generator函数，普通函数调用直接返回结果;generator函数返回一个generator对象


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)


o = odd()
next(o)
next(o)
next(o)
# next(o)
# odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。
# 执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。
g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break

# 练习
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：


def triangles():
    L = [1]
    while 1:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
