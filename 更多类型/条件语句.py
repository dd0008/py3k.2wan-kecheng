# 开发人：d
# 开发时间：2021/12/24,8:51
# 非零数值、非空字符串、非空list，判断为True。否则为False。
if True :
    print('hello python')
num = 6
if num :
    print('hello python')
num = ''
if num : # 空字符串，判断为False,不打印。
    print('hello python')

# 多个判断条件
res = 89
if res > 90:
    print('优秀')
elif res > 80:
    print('良好')
elif res > 60:
    print('及格')
else:
    print('不及格')

# 多个条件同时判断
java = 86
python = 68
if java >80 and python >80:
    print('优秀')
else:
    print('不优秀')

if (java >=80 and java < 90) or (python >=80 and python < 90): # 括号中的判断优先执行
# and和or的优先级低于>、<
    print('良好')

# 嵌套
if java > 80:
    if python > 80:
        print('优秀')
    else:
        print('不优秀')
else:
    print('不优秀')

# for 循环
for letters in 'hello 两点水':
    print(letters)

dict ={'一点水':"小学生",'两点水':'初中生','三点水':'高中生'}
for i in dict:
    print(i) # 只打印了字典 dict 中的每一个 key 值。

list = [123 , 456 , 789]
for i in list:
    print(i)

tuple = (1111, 2222, 3333)
for i in tuple:
    print(i)

set1 = set(['p','y','y','h','o','n'])
for i in set1:
    print(i)
'''总结：字符串、元组、列表、字典、集合，都可以放入for循环
但数字（整数、浮点数）不可以'''

# while循环
count = 1
sum1 = 0
while count <= 100:
    sum1 = sum1 + count
    count = count + 1
print(sum1) # 计算1-100所有整数的和

# for 用在迭代可迭代对象的情况
# while 用在满足一定条件时，反复执行的情况。（死循环+break退出）
# 部分情况下，for和while 可以互换
for i in range(0, 3):
    print(i)

i = 0
while i < 3:
    print(i)
    i = i + 1

count = 1
sum = 0
while (count <= 100):
    sum = sum + count
    if (sum > 1000): #当 sum 大于 1000 的时候用break退出循环
        break
    count = count + 1
print(sum)

count = 1
sum = 0
while (count <= 100):
    if (count % 2 == 0): # 双数时跳过输出
        count = count + 1
        continue
    sum = sum + count
    count = count + 1
print(sum)

count = 1
sum = 0
while (count <= 100):
    if (not count % 2 == 0): # 单数时跳过输出
        count = count + 1
        continue
    sum = sum + count
    count = count + 1
print(sum)

#这个例题逻辑混乱
for num in range(10,15):   # 迭代10到15（不包括15）之间的数字
    for i in range(2,num): # 根据上一个迭代因子迭代
        if num%i == 0:
            print('%d 是一个合数' % num)
            break          # 跳出当前循环
    else:
        print('%d 是一个质数' % num) # else会在循环正常执行完的情况下执行

# 这样简洁
for num in range(10,15):   # 迭代10到15（不包括15）之间的数字
    if num%2 == 0:
        print(num,'是一个合数' )
    else:
        print(num,'是一个质数' )

# 九九乘法表
for i in range(1,10):
    for j in range(1,1+i):
        print('{}x{}={}\t'.format(i, j, i*j), end='')
        # 大括号及其里面的字符(称作格式化字段)将会被.format()中的参数替换,注意有个点
    print()

# 判断是否是闰年
year = int(input('请输入一个年份：'))
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    # 公历年份是4的倍数，且不是100的倍数的。或者公历年份是整百数的，但必须是400的倍数。才是闰年
    print('{0}是闰年'.format(year))
else:
    print('{0}不是闰年'.format(year))













































