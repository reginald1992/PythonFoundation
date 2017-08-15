print(abs(-25))
print(max(1, 5, 25, -69, 63))
print(str(29.36415))
print(int(16.32))
print(bool(2))
print(bool(''))
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs  # 变量a指向abs函数
print(a(-35))


# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x


# 函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。 return None可以简写为return。
# 函数的调用：如果已经把my_abs()的函数定义保存为abstest.py文件了， 可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，
# 注意abstest是文件名（不含.py扩展名）


# 空函数
def nop():
    pass


# pass语句什么也不做，只是一个占位符，例如调试程序的时候，为了让程序先运行起来，可以用pass
age = int(input('age:'))
if age > 18:
    pass


# 函数的参数检查
# 当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善。
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 返回多个值：比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 60, 50, math.pi/6)
print('x=', x, 'y=', y)
# 实际上，返回的仍然是一个值
r = move(100, 60, 50, math.pi/6)
print(r)
# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

