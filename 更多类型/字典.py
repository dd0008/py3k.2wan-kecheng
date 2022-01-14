# 开发人：d
# 开发时间：2021/12/20,16:58

# 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号分割，整个字典包括在花括号{}中
ages = {'Dave':24,'Mary':42,'John':58} #字典中的每个元素都由键：值对表示
print(ages['Dave']) # 键值有点类似list或tuple中的元素下标索引
print(ages['Mary'])

primes = {1:2 , 2:3 , 4:7 , 7:17}
print(primes[primes[4]])

nums = {
    1:'one',
    2:'two',
    3:'three',
} #(),[],{}可以换行
print(1 in nums)
print('three' in nums) #只检查键，不检查键的值。
print(4 not in nums)

pairs = {1:"apple",
         'orange':[2,3,4],
         True:False,
         None:'True',}
print(pairs.get('orange'))
print(pairs.get(7))
print(pairs.get(12345 , '不在字典中')) #字典.get（）第二参数默认为None,也可以自定义第二参数

fib = {1:1 , 2:1 , 3:2 ,4:3} #最后一个键值对的逗号可以不写
print(fib.get(4,0)+fib.get(7,5)) #字典中没有7这个键，则返回第二参数做默认值

dict1 = {'liangdianshui':'11111', 'twowater':'22222', '两点水':'33333'}
print('\n',dict1)

del dict1['twowater'] # 通过key值删除对应元素
print(dict1)

dict1.clear() #删除字典中的所有元素
print(dict1)

del dict1 # 删除字典

dict1={'liangdianshui':'111111' ,'twowater':'222222' ,'两点水':'333333','twowater':'444444'}
print(dict1)
print(dict1['twowater']) # 不允许一个键创建两次的，但是如果出现了一个键被赋予了两次，会以最后一次赋予的值为准


dict1={'liang':'111' ,123:'222' ,(123,'tom'):'333','twowater':'444'}
print(dict1) # 键不可变，单键可以用数字，字符串或元组，但是不能使用列表


print(len(dict1)) # 计算字典元素个数
print(str(dict1)) # 输出字典可打印的字符串表示
print(type(dict1)) # 返回输入的变量类型，如果变量是字典就返回字典类型
print(dict.copy(dict1)) # 返回一个字典的浅复制
print(dict.values(dict1)) # 以列表返回字典中的所有值

print(dict.items(dict1)) # 以列表返回可遍历的(键, 值) 元组数组
print(dict.popitem(dict1)) # 随机返回并删除字典中的一对键和值
print(dict1)

print('\n1.set 的创建')
set1 = set([123, 456, 789]) # 创建一个 set，需要提供一个 list 作为输入集合
print(set1) # 输出的set用花括号显示，是无序的，
# dict也是无序的，只不过dict保存的是key-value键值对值，而set可以理解为只保存key值，不存储value值

set1 = set([123, 456, 789, 123, 123])
print(set1)  #在dict（字典）中有重复的key，会被后面的key-value值覆盖，而重复元素在set中也自动被过滤

set1 = set([123, 456, 789])
print(set1)
set1.add(100) # 添加元素到 set 中，可以重复添加，但不会有效果
print(set1)
set1.remove(456) # 删除 set 中的元素
print(set1)

set1 = set('hello') # set可以用字符串创建
set2 = set(['p','y','y','h','o','n']) # set可以用列表创建
print(set1)
print(set2)

# 交集
set3 = set1 & set2
print('\n交集 set3:')
print(set3)
#并集：合并且去重
set4 = set1 | set2
print('\n并集 set4:')
print(set4)
#差集:从本集中减去交集
set5 = set1 - set2
set6 = set2 - set1
print('\n差集 set5:')
print(set5)
print('\n差集 set6:')
print(set6)

# 去除海量列表里重复元素，用 hash 来解决也行，只不过感觉在性能上不是很高，用 set 解决还是很不错的
list1 = [111,222,333,444,111,222,333,444,555,666]
set7 = set(list1)
print('\n去除列表里重复元素 set7:')
print(set7)













































