"""
函数式编程--返回函数
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值进行返回
"""


# 可变参数的求和


def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算:可以不返回求和的结果，而是返回求和的函数


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 3, 5, 9)
print(f)
print(f())
# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：<function lazy_sum.<locals>.sum at 0x101c6ed90>
# 调用函数f时，才真正计算求和的结果
'''
在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1()和f2()的调用结果互不影响
'''

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)  # False
'''
闭包--NOTICE--返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
    （1）返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
    （2）返回的函数并没有立刻执行，而是直到调用了f()才执行，举例如下：
'''


def count():
    fs = []
    for i in range(1, 4):
        def f_temp():
            return i * i
        fs.append(f_temp)
    return fs


f1, f2, f3 = count()
print(f1, f2, f3)
print(f1(), f2(), f3())
'''
全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
'''


def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻执行，因此当前i的值被传进f(i)
    return fs


f4, f5, f6 = count()
print(f4(), f5(), f6())
