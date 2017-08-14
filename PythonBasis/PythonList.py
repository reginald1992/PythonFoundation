classmates = ['David', 'Bob', 'Tracy']  # list的使用
print(classmates)
len(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[-1])
classmates.append('Jack')
classmates.insert(2, 'Tim')
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(0)
print(classmates)
L = [True, 'James', 123, 15.263]
print(L)
s = [12, 'sdf sd', 26.33, [12, 26, 29], False]
print(s)
J = []
print(len(J))
classmates = ('Lucy', 'Jess', 'Jones', 'Tiger')  # tuple和list的不同之处在于tuple一旦初始化就不能做任何修改
# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。如果在tuple里面包含一个list，那么list中的元素可以变
print(classmates)
