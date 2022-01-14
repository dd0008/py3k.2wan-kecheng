# 开发人：d
# 开发时间：2021/12/21,11:52

#列表切片
squares = [0,1,4,9,16,25,36,49,64,81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

print('第四行',squares[1:-1])
'''squares这个列表元素的下标是[0,1,2,3,4,5,6,7,8,9],
或者用负数表示[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1],下标-1相当于9
'''
print(squares[:2]) #省略第一个数字，默认从开始
print(squares[2:]) #省略第一个数字，默认到结尾
print(squares[:])  #省略第一个和第二个数字，拿全列
print(squares[::3]) #第三个数步进，省略时默认为1

print('第九行',squares[::-1]) #步进为负，从末尾开始计数。即反转列表
# 反转列表另一个写法:
print(squares.reverse())
print(squares[7:5:-1]) #当步进为负时，第一个数要大于第二个数；步进为正时，则相反。
print(squares[5:7:-1])  #这个是错误的写法，会返回一个空列表

#列表推导式（列表与range）
cubes = [i**3 for i in range(5)] # 用for in range()生成一个列表，列表的每个元素三次方
print('第11行',cubes)

print('生成从0到18的偶数',[i*2 for i in range(10)])
print([i**2 for i in range(10) if i**2 % 2 == 0]) #用if语句增加强制条件

a = [0,1,2,3,4,5,6,7,8,9]
print([i*-1 for i in a])
print([i*-1 for i in [7,8,9]]) #将列表里每个元素*一个数

user = ['liangdianshui','twowater','两点水']
print('1.产品用户')
print(user)

len(user)
print('\n2.统计有多少个用户')
print(len(user))

print('\n3.查看具体的用户')
print(user[0] + ',' + user[1] + ',' + user[2])

user.append('茵茵')
print('\n4.在末尾添加新用户')
print(user)

user.insert(0,'VIP用户')
print("\n5.在指定位置插入用户")
print(user)

user.pop()
print('\n6.删除末尾用户')
print(user)

user.pop(1)
print('\n7.删除指定位置的list元素')
print(user)

user[2] = '三点水'
print('\n8.把某个元素换成别的元素')
print(user)

newuser = [['VIP用户',11111] , ['twowater',22222] , ['三点水',33333]]
print('\n9.不同元素类型的list数据')
print(newuser)