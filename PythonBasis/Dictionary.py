# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85, 'Adams': 67}
# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
d['James'] = 99
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
d['James'] = 80
print(d['James'])
# 如果key不存在，dict就会报错;要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('Lucy' in d)
print('Bob' in d)
# 二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Thomas'))
print(d.get('Thomas', -1))
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Bob')
print(d)
# dict内部存放的顺序和key放入的顺序是没有关系的
# 和list比较，dict有以下几个特点：
# 1、查找和插入的速度极快，不会随着key的增加而变慢；
# 2、需要占用大量的内存，内存浪费多。
# 而list相反：
# 1、查找和插入的时间随着元素的增加而增加；
# 2、占用空间小，浪费内存很少。
# 正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象
# 在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key

# set与dict类似，也是一组key的组合，但是不存储value
# 创建set的时候，需要提供一个list作为输入集合
s = set([1, 2, 3])
# 通过add（key）和remove（key）可以增减元素
s.add(4)
print(s)
s.remove(4)
print(s)
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([2, 4, 6, 8, 10])
s2 = set([1, 2, 3, 4, 5])
print(s1 & s2)
print(s1 | s2)

# 不可变对象
a = 'abc'
a.replace('a', 'A')
print(a)
