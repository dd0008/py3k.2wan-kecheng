# 开发人：d
# 开发时间：2021/12/29,11:19

# 定义类
class classA():
    var1 = 100
    var2 = 0.01
    var3 = '两点水'

    def fun1():
        print('我是fun1')

    def fun2():
        print('我是fun2')

    def fun3():
        print('我是fun3')

# 调用类
print(classA.var1)
print(classA.var2)
print(classA.var3)
classA.fun1()
classA.fun2()
classA.fun3()

# 类方法
# 类方法调用类属性
class ClassA():
    var1 = '两点水'

    @classmethod #声明以下函数是类方法，只有声明了，才能使用类属性
    def fun1(cls): #类方法想要使用类属性，在第一个参数中，需要写上 cls , cls 是 class 的缩写，
                   # 其实意思就是把这个类作为参数，传给自己，这样就可以使用类属性了
        print('我是fun1' + cls.var1) # 类属性的使用方式就是 cls.变量名
# 无论是 @classmethod 还是 cls ,都是不能省去的。省了都会报错
ClassA.fun1()

# 类方法传参
class ClassA():
    var1 = '两点水'

    @classmethod
    def fun1(cls, age): # 定义了一个age参数
        print('我是fun1' + cls.var1)
        print('年龄：' + str(age))

ClassA.fun1(18) # 多了个参数

# 四、修改、增加类属性
# 1、从内部增加和修改类属性
class ClassA():
    var1 = '两点水'
    @classmethod




















