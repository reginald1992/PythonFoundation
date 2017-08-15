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
# 函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
# return None可以简写为return。
