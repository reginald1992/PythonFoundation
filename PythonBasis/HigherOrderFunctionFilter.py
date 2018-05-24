# -*- coding: utf-8 -*-
"""
Created on Thu May 24 16:45:57 2018

@author: Shulin Liu
"""

'''
Higher-order function: filter()过滤序列

Python内建的filter()函数用于过滤序列。
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，
filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
filter()的核心在于“筛选”
注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，
需要用list()函数获得所有结果并返回list。
'''

#在一个list中删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8])))

#将一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

#用filter求素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
#上述是一个生成器，且是一个无限序列，以下定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0
#最后，定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() #初始序列
    while True:
        n = next(it)
        yield n 
        it = filter(_not_divisible(n), it) # 构造新序列
#由于primes也是一个无限序列，设置一个条件退出循环
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
#注意到Iterator是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁。

'''
练习：数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
'''
from functools import reduce
def is_palindrome(n):
    pass
    