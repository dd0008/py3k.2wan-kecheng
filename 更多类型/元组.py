# 开发人：d
# 开发时间：2021/12/23,15:34

# 元组：在小括号（）中添加元素，并使用逗号隔开
print('\n1.元组：在小括号（）中添加元素，并使用逗号隔开')
tuple1 = ('两点水', 'twowater', 'liangdianshui', 123, 456)
tuple2 = '两点水', 'twowater', 'liangdianshui', 123, 456
# 也可以不用括号，只用逗号分隔即可。
tuple3 = ()
tuple4 = (123,) # 只有一个元素，要加逗号。
tuple5 = (123) # 只有一个元素，不加逗号默认按数学小括号处理。
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
print(tuple5)

# 访问元组
print('\n2.访问元组')
print(tuple1[0])

print('\n3.修改元组') # 元组不可修改是指元组中的元素值不允许修改，
# 但可以对元组进行连接组合，还有通过修改其他列表的值从而影响 tuple 的值，
# 即可以对元组中元素中的元素进行修改。
list1 = [13, 46]
tuple1 = ('两点水', 'twowater', 'liangdianshui', list1)
print(tuple1)
list1[0] = 789
list1[1] = 100
print(tuple1)

print('\n4.删除元组') # 元组中的元素值是不允许删除的，但可以用 del 语句来删除整个元组
tuple1=('两点水','twowter','liangdianshui',[123,456])
print(tuple1)
del tuple1

print('\n5.元组运算符')
print((1, 2, 3) + (4, 5, 6))
print(('Hi!',) * 4)
print(len((1, 2, 3)))
print(3 in (1, 2, 3))
for x in (1, 2, 3): print(x)

list1 = [1, 2, 3]
print(list1)
a = tuple(list1) # 将列表转换为元组
print(a)



























