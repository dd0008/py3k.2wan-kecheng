# 开发人：d
# 开发时间：2021/12/21,15:02

print('/'.join(['spam','eggs','ham'])) # join将一个字符串添加到另一个字符串列表的分隔符位置，并将列表转为字符串。
print('spam/eggs/ham'.split('/')) #split用逗号将字符串按照特定符号(比如/)分开，并将字符串转为列表。

print('hello me'.replace('me','world')) # replace替换一个字符串hello me中的一个子字符串me
print('this is a sentence'.startswith('this')) #确定字符串的开始是否有子字符串
print('this is a sentence'.endswith('sentence'))
print('this is a sentence'.upper()) # 英文转换为大写
print('This is A Sentence'.lower()) # 英文转换为小写

print('这里是第1个分割线————————————')

print(min(1,2,3,4,0,2,1)) #可以是一些数字
print(max([1,4,9,2,5,6,8])) #可以是一个列表
print(abs(-99))

print(sum([1,2,3,4,5]))
#print(sum(1,2,3,4,5)) 错误

print('这里是第2个分割线————————————')
# all、any、enumerate
nums = [55,44,33,22,11]
if all([i>5 for i in nums]): #所有
    print('All larger than 5')
if any([i%2==0 for i in nums]): #只要有一个
    print('At least one is even')
for v in enumerate(nums): #enumerate()枚举函数，可遍历列表的索引和值
    print(v)

nums = [-1,2,-3,4,-5]
if all([ abs(i) <3 for i in nums]):
    print(1)
else:
    print(2)




