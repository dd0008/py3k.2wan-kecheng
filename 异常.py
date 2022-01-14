# 开发人：d
# 开发时间：2021/12/20,12:38
try:
    num1 = 7
    num2 = 1
    print(num1/num2)
    print('计算完毕')
except ZeroDivisionError:
    print('发生了一个错误')
    print('一个除以0的错误')

try:
    print(1+1)
except ZeroDivisionError:
    print('不能除以0')

try:
    print(1/2)
except ZeroDivisionError:
    raise ValueError

try:
    print(1)
except: #没有发现异常，则不执行except
    print(2)
finally: #不管上面出现什么错误，都执行下面的代码
    print(3)

try:
    print('hello')
    print(1/0)
except ZeroDivisionError:
    print('0不能做分母')
finally:
    print('这条必须运行')

print(1)
#raise ValueError #这一句导致后面行的代码都无法运行
print(2)

try:
    print(1/0)
except ZeroDivisionError: #显示除0错误
    print('除0错误') #try/except的下一行必须缩进，不然会出现IndentationError
    #raise ValueError #人工抛出一个ValueError

#num = input(':')
#if float(num) < 0:
    #raise ValueError('负数') #如果用户输入小于0，则报错并输出‘负数’。

print(1)
assert 2 + 2 == 4
print(2)
#assert 1 + 1 == 3 #在程序中置入检查点，确保某个条件必须为真，才能让程序正常工作。
print(3)

temp = -10
#assert (temp>=0) , '在0以下' #‘‘在0一下’是assert的第二个参数’
#assert与raise如果不缩进会导致后面代码无法运行。

#def my_func(x):
    #assert x>0 , 'Error!'
#print(x)

try:
    print(1)
    assert 2+2==5
except AssertionError:
    print(3)
except:
    print(4)




print('hao')

