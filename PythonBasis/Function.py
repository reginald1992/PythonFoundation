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


x, y = move(100, 60, 50, math.pi / 6)
print('x=', x, 'y=', y)
# 实际上，返回的仍然是一个值
r = move(100, 60, 50, math.pi / 6)
print(r)


# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

# practice
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0
# 的两个解。


def quadratic(a, b, c):
    s = float(b * b - 4 * a * c)
    if s < 0:
        print('该方程式无解')
    else:
        x1 = (math.sqrt(s) - b) / (2 * a)
        x2 = (math.sqrt(s) + b) / (2 * a)
        return x1, x2


# Python函数的参数设置
def power(x):
    return x * x


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
        return s


# 修改后的函数可以计算任意次方


# 此时可以发现，之前写的power函数失效了，会给出参数数目不正确的警告。需要设置默认的参数


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 这样在输入power（5）的时候，相当于调用power（5,2），如果要计算其他的，则必须明确传入n
# 设置默认参数时，有几点要注意：
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 二是如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。

# 举例说明：小学生登记信息
def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)


# 大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数，只有与默认参数不符的学生才需要提供额外的信息：
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7)，意思是，
# 除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。
# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。
# 比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。

