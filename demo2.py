# 开发人：d
# 开发时间：2021/12/16,13:03

#转义字符
print('hello\nworld')
print('helloooo\nworld') #\n换行，new line，光标移动到下一行的开头
print('hello\tworld') #\t水平制表符，tab，光标移动到下一组4个空格的开始处
print('helloooo\tworld')
print('hello\rworld') #\r回车，，将hello覆盖了，return 光标移动到本行的开头
print('hello\bworld') #\b退格,将o退没了，back space
print('http:\\\\www.baidu.com')
print('老师说：”大家好“')
print("老师说：”大家好“")
print("老师说：'大家好'")
print("老师说：\"大家好\"") #第一字符串必须用英文状态的单或双引号。第二如果引号里面套引号，要么两对引号不同，要么在内部引号前加\

#原字符r或R
print(r"老师说：\"大家好\"") #r或R是原字符，可以让转义字符\失去转移功能，而作为普通字符显示。
#print(r"老师说：\"大家好\"\") 但要注意，这样会报错，因最后一个字符不能是反斜杠。
print(r"老师说：\"大家好\"\\") #但，可以是两个反斜杠。
#foo=input("请输入一个数：")
#print(foo)
x=2
print(x)
x+=3
print(x)
print(2==3)
print(2==2)
if 7>5:
    print(5)

x = 4
if x==5:
    print("yes")
else:
    print("no")

num = 7
if num == 5:
    print("number is 5")
elif num == 7:
    print("number is 7")
elif num ==11:
    print("number is 11")
else:
    print("num既不是5或7，也不是11")

i = 1
while i <= 5:
    print(i)
    i=i+1
print("结束")

i = 0
while 1==1:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break

print("Finished")

i=5
while True:
    print(i)
    i =i -1
    if i <=2:
        break

i = 0
while True:
    i =i + 1
    if i == 2:
        print("Skipping 2")
        continue #流程到此结束，返回继续循环while
    if i == 5:
        print("Breaking")
        break #while流程到此结束，跳出while继续执行后面的流程；因此不打印5
    print(i)
print('Finished')

i = 0
while i <5:#注意与上一条对比：删除Break功能将变无限循环，所有要限制i的最大值。
    i =i + 1
    if i == 2:
        print("Skipping 2")
        continue #流程到此结束，返回继续循环while
    if i == 5:
        print("Breaking")
        #break #删除Break功能。
    print(i)
print('Finished')

str = 'hello  world!'
print(str[7])

nums = [1,2,3] #列表与字符串相似。字符串可以看作是不能更改的列表。
print(nums + [4,5,6])
print(nums * 3)
print(1 in nums)
print(5 in nums)
print(max(nums))

words = ['python','fun']
index = 1
words.insert(index,'is')
print(words)

letters = ['p','q','r','s','p','u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.count('p'))
letters.remove('q') #将q从列表中移除，相当于对letters重新定义
print(letters)
#print(letters.index('z')) #项目不在列表中（超出列表范围），会出错，导致后面行无法运行。
letters.reverse() #反向列表中元素，相当于对letters重新定义
print(letters)

words = ['hello','world','spam','eggs']
counter = 0
max_index =len(words)-1
while counter <= max_index:
    word = words[counter]
    print(word + '!')
    counter = counter + 1

words = ['hello','world','spam','eggs']
a = 0
b = 3
while a <= b:
    word = words[a]
    print(word + '!')
    a = a + 1

words = ['你好','世界','spam','eggs']
for tt in words: #每循环一次将words中的一项依次赋值给tt,直到遍历所有项。
    print(tt + '!')

for i in range(5): #for不需要调用列表（即不需要事先转为列表）;
    print(i)
    print('hello!')

# 输出0到20的偶数
for i in range(0,20,2): # range(20)相当于range(0,20),但都不包括20（即所谓的左开右闭）
    print(i)

# 输出2到10的偶数
for i in range(10): # 相当于0-9，[0,1,2...,9,10]
    if not i % 2 == 0:
        print(i+1)

# 自定义函数
def hello(): # 定义函数
    print("东西南北中") # 打印在函数之内，所以调用函数时不用再print就能显示。
hello() # 调用函数

def p_double(x):
    print(2*x)
p_double("d")

def p_double(x):
    print(2*x)
p_double(3)

# 一旦从函数返回一个值，它就停止执行后面的代码。
def add_nums(x,y):
    total = x + y
    return total
    print('这个不会被打印')
print(add_nums(4,5))


def print_num():
    print(1)
    print(2)
    return
    print(4) #return后面的代码不会被执行

print(5)

# 文档字符
def shout(word):
    '''打印字符并在后面
    加上感叹号 （可以多行）'''
    print(word + "!")
shout('spam')

# 函数重新赋值
def multiply(x,y):
    return x * y
a = 4
b = 7
ope = multiply #注意没有括号
print(ope(a,b))

def shortest_string(n,m):
    if len(n) <= len(m): # len(s),s可以是字符串、列表、元组。
        return n #return后没有括号
    else:
        return m #return后没有括号
print(shortest_string('abc','d')) #1.不加print(),不能显示结果，为什么？因为return返回的不是显式
                                  # 2.字符不加引号，也不显示结果。

# import module_name 引用模块
import random
for i in range(5): # 给i返回一个值依次为0、1、2、3、4，需返回5次；但并不是使用i这个对象，只是利用它的返回次数
    value = random.randint(1,6) # 随机生成一个整数(范围包括1和6)，并赋值给value
    print(value)

import random
result = random.randint(1,10) # random.randint()随机返回一个整数,且不可迭代
print('result:',result)
# print(list(result)) #所以这句用list（）是错误的。

# range()与list()的区别
a = range(0,5) # range()返回的是一个对象,而且是可迭代的对象
print(a) # range()与random模块random.randint（）的区别。
print(list(a)) # 但可以用list()转为列表

import math
num = 9
print(math.sqrt(num))

from math import pi # 只从math模块中导入pi这个变量
print(pi) # 如果没有上面一句，这一句不能运行。

from math import sqrt # 只从math模块中导入sqrt这个变量
print(sqrt(2))# 如果没有上面一句，这一句不能运行。

from math import  sqrt as i  # 也可以将它赋值给一个自定义简化的变量名
print(i(100))
print(sqrt(100)) #sqrt()依然可以使用。

import math as m
print(math.sqrt(25))
print(m.sqrt(25))

def print_nums(x):
    for i in range(x):
        print(i)
        return #只能打印出0。因为return缩进后，处于for循环内，导致了for循环运行第一次之后就结束了。
print_nums(10)

def func(x):
    res = 0
    for i in range(x):
        res += i # 注意这里是将i加给res,而不是将1加给res
        #return res # 如果return缩进到for循环中，将只能返回0
    return res # return在for循环外,直到for循环结束后再执行return
print(func(4))

for i in range(4):
    print(i)