# 在Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。
# ----------------------------------------------------------------------------------------------------------------------
# 高级特性之一：切片（slice）
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

# ----------------------------------------------------------------------------------------------------------------------
# 高级特性之二：迭代（iteration）
# 如果给定一个list或tuple，可以通过for循环遍历这个list或tuple,在Python中迭代是通过for循环完成的，而很多的语言是通过下标完成的
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


def findMinAndMax(L):
    if len(L) < 1:
        return None, None
    else:
        min = max = L[0]
        for element in L:
            if element > max:
                max = element
            if element < min:
                min = element
        return min, max
# 测试


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
