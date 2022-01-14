# 开发人：d
# 开发时间：2021/12/28,8:46

#一、迭代
#1、for循环迭代字符串
for char in 'liangdianshui' :
    print(char, end=' ')
print('\n')

#2、for循环迭代list
list1 = [1, 2, 3, 4, 5]
for num1 in list1:
    print(num1, end=' ')
print('\n')

#3、for循环也可以迭代dict(字典)
dict1 = {'name':'两点水', 'age' : '23', 'sex' : '男'}
for key in dict1: #迭代dict中的key
    print(key, end= ' ')
print('\n')

for value in dict1. values(): #迭代dict中的value
    print(value, end=' ')
print('\n')

#如果list里一个元素有两个变量：
for x, y in [(1,'a'), (2, 'b'), (3, 'c')]:
    print(x, y)

# 二、迭代器
# 1、字符串创建迭代器对象
str1 = 'liangdianshui'
iter1 =iter(str1)

# 2、list对象创建迭代器
list1 =[1,2,3,4]
iter2 = iter(list1)

# 3、tuple(元组)对象创建迭代器
tuple1 = (1,2,3,4)
iter3 = iter(tuple1)

# for循环遍历迭代器对象
for x in iter1 :
    print(x, end=' ')

print('\n-------------------')

# next()函数遍历迭代器
while True :
    try:
        print(next(iter3))
    except StopIteration :
        break

# 三、list 生成式
# 1、创建list的方式
list1 = list(range(1, 31))
print(list1)

# 2、list生成式的创建
list1 = [x * x for x in range(1, 11)]
print(list1)

list1 = [x * x for x in range(1,11) if x%2 == 0]
print(list1)

# for 循环里面也嵌套 for 循环
list1 = [(x + 1, y + 1) for x in range(3) for y in range(5)]
print(list1)
#当第一个for每遍历一个值后，第二个for就遍历一遍。

# 四、生成器
# 创建生成器 []改为（）
gen = (x * x for x in range(10))
print(gen)
# 创建 List 和 generator 的区别仅在于最外层的 [] 和 ()
'''生成器并不真正创建数字列表， 而是返回一个生成器，生成器在每次计算出一个条目后，
把这个条目“产生” ( yield ) 出来。
生成器表达式使用了“惰性计算” ( lazy evaluation)，
只有在检索时才被赋值(evaluated)，所以在列表比较长的情况下使用内存上更有效'''

gen = (x * x for x in range(10))

for num in gen :
    print(num)

# 函数创建生成器
def my_function():
    for i in range(10):
        print(i)

my_function()
print('------------------')

# 将上面例子修改后就变成生成器
def my_function():
    for i in range(10):
        yield (i)

my_function()
print(my_function())

# 计算斐波那契数列的生成器
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
# 引用函数
for x in fibon(1000):
    print(x, end=' ')
print('\n------------------')

#变形
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

m = 0
for t in fibon(1):
    print(t)
    m = m + 1
    if m == 10:
        break

'''最难理解的就是 generator 和函数的执行流程不一样。函数是顺序执行，
遇到 return 语句或者最后一行函数语句就返回。而变成 generator 的函数，
在每次调用 next() 的时候执行，遇到 yield语句返回，
再次执行时从上次返回的 yield 语句处继续执行。
比如这个例子：'''
def odd():
    print ( 'step 1' )
    yield ( 1 )
    print ( 'step 2' )
    yield ( 3 )
    print ( 'step 3' )
    yield ( 5 )

o = odd()
print( next( o ) )
print( next( o ) )
print( next( o ) )

#打印杨辉三角
def triangles(n):
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L [i - 1] + L [i] for i in range(len(L))]

n = 0
for t in triangles(10):
    print(t)
    n = n + 1
    if n == 10:
        break

# 五、迭代器和生成器综合例子
# 1、反向迭代
list1 = [1, 2, 3, 4, 5]
for num1 in list1:
    print(num1, end=' ')
print('\n')

list1 = [1, 2, 3, 4, 5]
for num1 in reversed(list1):
    print(num1, end=' ')
print('\n')#Python换行

# 2、同时迭代多个序列
names = ['liangdianshui', 'twowater', '两点水', '三点水']
ages = [18, 19, 20]
for name, age in zip(names, ages):
    print(name, age)

# zip(a, b) 会生成一个可返回元组 (x, y) 的迭代器，其中 x 来自 a，y 来自 b。
# 一旦其中某个序列到底结尾，迭代宣告结束。 因此迭代长度跟参数中最短序列长度一致。

names = ['liangdianshui', 'twowater', '两点水', '三点水']
ages = [18, 19, 20]
dict1 = dict(zip(names, ages))
print(dict1)







