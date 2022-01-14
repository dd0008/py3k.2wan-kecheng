# 开发人：d
# 开发时间：2021/12/20,16:41

#None
a = ''
b = False
c = []
d = 0
print(a == None)
print(b == None)
print(c == None)
print(d == None)

foo = print()
if foo == None: #None是空，是一个类型，也是一个对象
    print(1)
else:
    print(2)

#lambda
print((lambda x: x**2 + 5*x + 4)(-4))