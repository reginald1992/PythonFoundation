"""
匿名函数：在传入函数时，不需要显式地定义函数，直接传入匿名函数lambda
"""
a = list(map((lambda x: x * x), [1, 2, 3, 4, 5, 6, 7]))


def f(x):
    return x * x


'''
匿名函数lambda x: x * x实际上和上述的函数f(x)是一致的，关键字lambda表示匿名函数，冒号前面的x表示函数参数
匿名函数的限制：只能有一个表达式，不用写return，返回值就是表达式的结果
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
'''
g = lambda x: x * x
print(g(5))
# 可以把匿名函数作为返回值返回


def build(x, y):
    return lambda: x * x + y * y


'''
练习：用匿名函数改造一下代码
'''


def is_odd(n):
    return n % 2 == 1


L1 = list(filter(is_odd, range(1, 20)))
# 使用lambda优化
L2 = list(filter(lambda n: n % 2 == 1, range(1, 20)))
