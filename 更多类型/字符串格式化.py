# 开发人：d
# 开发时间：2021/12/21,14:33

nums = [4,5,6]
msg = 'Numbers:{0} {1} {2}'.format(nums[0],nums[1],nums[2]) #引号内大括号内数字为列表中元素的索引，其余为自定义文字。
print(msg)

print('{0}{1}{0}'.format('ab','ef')) # format()内是列表的元素

a = '{x},{y}'.format(x=5, y=12)
print(a)