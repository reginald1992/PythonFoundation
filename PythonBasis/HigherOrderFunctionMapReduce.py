# -*- coding: utf-8 -*-
"""
Created on Wed May 23 20:11:32 2018

@author: Shulin Liu
"""

'''
Functional Programming
函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数调用，
就可以把复杂任务分解成简单的任务，这种分解可以称之为面向过程的程序设计。函数就是面向过程的程序设计的基本单元。
而函数式编程（请注意多了一个“式”字）——Functional Programming，虽然也可以归结到面向过程的程序设计，但其思想更接近数学计算。
我们首先要搞明白计算机（Computer）和计算（Compute）的概念。
在计算机的层次上，CPU执行的是加减乘除的指令代码，以及各种条件判断和跳转指令，所以，汇编语言是最贴近计算机的语言。
而计算则指数学意义上的计算，越是抽象的计算，离计算机硬件越远。
对应到编程语言，就是越低级的语言，越贴近计算机，抽象程度低，执行效率高，比如C语言；
越高级的语言，越贴近计算，抽象程度高，执行效率低，比如Lisp语言。
函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，
因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。
而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。
函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。
'''


# TODO 函数式编程之一：高阶函数 Higher-order function


print(abs)
x = abs(-10)
print(x)
f = abs
print(f)
print(f(-10))

'''
函数本身可以赋值给变量，即：变量可以指向函数---函数名也是变量
既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
函数式编程指的就是这种高度抽象的编程范式
'''


def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))

'''
TODO 函数式编程之一：高阶函数 map/reduce
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6])

list(r)
# map()作为高阶函数，事实上把运算规则抽象化了
list(map(str, [1, 2, 3, 4, 5, 6]))

# 使用reduce（）可以一行代码解决累加问题
from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# 把序列[1, 3, 5, 7, 9]转化成13579
def fn(x, y):
    return x * 10 + y


a = reduce(fn, [1, 3, 5, 7, 9])


# 如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，就可以写出把str转换为int的函数：
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


b = reduce(fn, map(char2num, '123456789'))
print(b)

# 编写一个str2int的函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(fn, map(char2num), s)


# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    n = s.find('.')
    print(n)
    n = len(s) - n - 1
    print(n)
    a = reduce(lambda x, y: 10 * x + y, map(int, s.replace('.', '')))
    return float(a) / pow(10, n)


test = str2float('23659.3')
print(test)
