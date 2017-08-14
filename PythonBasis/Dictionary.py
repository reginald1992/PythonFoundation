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
# dict内部存放的顺序和key放入的顺序是没有关系的
# 和list比较，dict有以下几个特点：
# 1、查找和插入的速度极快，不会随着key的增加而变慢；
# 2、需要占用大量的内存，内存浪费多。
# 而list相反：
# 1、查找和插入的时间随着元素的增加而增加；
# 2、占用空间小，浪费内存很少。
# 正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象
# 在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key




