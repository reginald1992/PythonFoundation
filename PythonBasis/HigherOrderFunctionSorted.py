"""
排序算法：排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？
直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。
"""
temp1 = sorted([36, -25, 36, 26, 3, -6])
'''
sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
'''
temp2 = sorted([36, -25, 36, 26, 3, -6], key=abs)
temp3 = sorted(['bob', 'about', 'Zoo', 'Credit'])
'''
默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
现在，我们提出排序应该忽略大小写，按照字母序排序。
'''
temp4 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
temp5 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
'''
小结与练习
假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：
'''
# -*- coding: utf-8 -*-
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return -t[1]


L3 = sorted(L, key=by_score)
print(L3)
