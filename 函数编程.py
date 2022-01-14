# 开发人：d
# 开发时间：2021/12/21,17:04

'''
def 函数名(参数1，参数2....参数n):
    函数体
    return 语句
'''
#return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的 return 相当于返回 None

def division(num1,num2):
    #求商与余数
    a = num1 % num2
    b = (num1 - a) / num2
    return b , a
f = division(9,4)
tuple1 = division(9,4) #Python 一次接受多个返回值的数据类型就是元组。
print(f)
print(tuple1)

#默认参数
def print_user_info(name, age, sex = '男'):
    #打印用户信息
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别:{}'.format(sex))
    return
# 调用 prprint_user_info 函数
print_user_info('两点水', 18, '女')
print_user_info('三点水', 25) # 默认参数只能是末尾参数。

def print_info(a, b = None):
    if b is None :
        b = []
    print(b)
    return b ;
result = print_info(1)
result.append('error')
print_info(2)

#关键字参数。可以不按顺序
def print_user_info(name, age, sex = '男'):
    # 打印用户信息
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex))
    return
# 调用print_user_info函数
print_user_info(name='两点水',age= 18,sex= '女')
print_user_info(name='两点水',sex= '女',age= 18)

'''匿名函数主要有以下特点：
lambda 只是一个表达式，函数体比 def 简单很多。
lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。'''

sum = lambda num1, num2 : num1 + num2;
print(sum(1,2))

'''匿名函数中，有一个特别需要注意的问题，比如，把上面的例子改一下：'''
num2 = 100
sum1 = lambda num1 : num1 + num2;

num2 = 10000
sum2 = lambda num1 : num1 + num2;

print(sum1(1))
print(sum2(1))
'''你会认为输出什么呢？第一个输出是 101，第二个是 10001，结果不是的，输出的结果是这样：
10001
10001这主要在于 lambda 表达式中的 num2 是一个自由变量，在运行时绑定值，
而不是定义时就绑定，这跟函数的默认值参数定义是不同的。
所以建议还是遇到这种情况还是使用第一种解法。'''





























def aa (func , arg):
    return func (func (arg))
def myfive(x):
    return x +5
print(aa (myfive , 10)) #==myfive(myfive(10))

#纯函数
def pure_function (x , y):
    temp = x + 2*y
    return temp / (2*x + y)
print(pure_function(2,9))

#不纯函数
some_list = []
def impure(arg):
    some_list.append(arg) #改变了原列表的状态
some_list.append('haha')
print(some_list)

#lambda 匿名函数lambda arg1 ,arg2,.....argn:expression
def pol(x):
    return x**2 + 5*x + 4
print(pol(-4))

#等价于
print((lambda x: x**2 + 5*x + 4) (-4)) #全句无逗号

print('这里开始map、filter')
#map 映射
def add_five(x):
    return x + 5
nums = [11,22,33,44,55]
result = list(map(add_five,nums)) #map（函数，迭代参数），将参数（列表内元素）依次提供给函数。
print(result)

nums = [11,22,33,44,55]
result = list(map(lambda x: x+5,nums))
print(result)

#filter 过滤器 留下符合要求的
nums = [11,22,33,44,55]
result = list(filter(lambda x: x%2==0,nums))
print(result)

#Generatorsd 使用了 yield 的函数被称为生成器（generator）

def exp():
    x = 1
    return x
    return x + 1 #上一句return返回结果并终止运行，所以本句不运行

print(exp())

def exp():
    x = 1
    yield x
    yield x + 1 #上一句yield返回结果并保留变量，继续运行下一句，所以本句运行
    yield x + 2

for i in exp() :
    print(i)

def exp():
    x , y = 1 , 10
    while x < y :
        yield x
        x += 1
for i in exp() :
    print(i)







#装饰器Decorators
def decor(func): #3、函数2，打印一行分割线，执行函数1，再打印一行分割线
    def wrap():
        print("==========")
        func()
        print("==========")
    return wrap
def print_text(): #1、函数1，打印hello
    print('hello world!')
decorated = decor(print_text) #2、将函数1作为函数2的参数
decorated()

@decor #用@调用前面已经定义过的decor函数
def print_text():
    print('hello world!')
print_text()











