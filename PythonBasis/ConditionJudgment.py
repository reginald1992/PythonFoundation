s = input('age:')
age = int(s)
if age > 18:
    print('Your age is ', age)
    print('adult')
else:
    print('Your age is ', age)
    print('teenager')
b = input('birth: ')
birth = int(b)
if birth < 2000:
    print('00前')
else:
    print('00后')
    # practice
    # 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
    # 低于18.5：过轻
    # 18.5-25：正常
    # 25-28：过重
    # 28-32：肥胖
    # 高于32：严重肥胖
    # 用if-elif判断并打印结果
h = input('height:')
height = float(h)
w = input('weight:')
weight = float(w)
bmi = weight / height / height
if bmi > 32:
    print('严重肥胖')
elif bmi > 28:
    print('肥胖')
elif bmi > 25:
    print('过重')
elif bmi > 18.5:
    print('正常')
else:
    print('过轻')
