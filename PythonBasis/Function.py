print(abs(-25))
print(max(1, 5, 25, -69, 63))
print(str(29.36415))
print(int(16.32))
print(bool(2))
print(bool(''))
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs  # 变量a指向abs函数
print(a(-35))


# ———————————————————————————————————————————————————————————
# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x


# 函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。 return None可以简写为return。
# 函数的调用：如果已经把my_abs()的函数定义保存为abstest.py文件了， 可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，
# 注意abstest是文件名（不含.py扩展名）

# ———————————————————————————————————————————————————————————
# 空函数
def nop():
    pass


# pass语句什么也不做，只是一个占位符，例如调试程序的时候，为了让程序先运行起来，可以用pass，这在实际调试程序的时候常常用到
# if age > 18:
#     pass


# ———————————————————————————————————————————————————————————
# 函数的参数检查
# 当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善。
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# ———————————————————————————————————————————————————————————
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


# ——————————————————————————————————————————————————————————
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
# 谨防默认参数的大坑：定义默认参数要牢记一点：默认参数必须指向不变对象！下面举例说明：
# 先定义一个函数，传入一个list，添加一个END再返回：
# def add_end(L=[]):
#     L.append('END')
#     return L
# 当你正常调用时，结果似乎不错：
#
# >>> add_end([1, 2, 3])
# [1, 2, 3, 'END']
# >>> add_end(['x', 'y', 'z'])
# ['x', 'y', 'z', 'END']
# 当你使用默认参数调用时，一开始结果也是对的：
#
# >>> add_end()
# ['END']
# 但是，再次调用add_end()时，结果就不对了：
#
# >>> add_end()
# ['END', 'END']
# >>> add_end()
# ['END', 'END', 'END']
# 很多初学者很疑惑，默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。
#
# 原因解释如下：
#
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
# 如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#
# 所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
#
# 要修改上面的例子，我们可以用None这个不变对象来实现：
#
# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
# 现在，无论调用多少次，都不会有问题：
#
# >>> add_end()
# ['END']
# >>> add_end()
# ['END']
# 为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，
# 这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。
# 我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

# ——————————————————————————————————————————————————————————
# 可变个数的形参
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
nums = [1, 2, 3]
calc(nums[0], nums[1], nums[2])
# 这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
nums = [1, 2, 3]
calc(*nums)


# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。


# ——————————————————————————————————————————————————————————
# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# 函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
person('Michael', 26)
# 也可以传入任意个数的关键字参数：
person('Bob', 25, city='Beijing')
person('Adam', 20, gender='M', job='Engineer')
# 关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，
# 但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，
# 其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jake', 28, **extra)


# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra


# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些参数，就需要在函数内部通过kw检查。
# 仍然以person（）为例，我们检查是否有city和job参数：
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('names:', name, 'age', age, 'other', kw)


# 但是调用者仍可以传入不受限制的关键字参数
person('Jack', 24, city='Beijing', addr='HaiDian', zipcode=123456)


# ---------------------------------------------------------------------------------------------------------------------
# 命名关键字参数：
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接受city和job作为关键字。定义方式如下：
def person(name, age, *, city, job):
    print(name, age, city, job)

# 与关键字参数**kw不同，命名关键字参数需要一个特殊的分隔符*，*后面的参数被视为命名关键字参数
