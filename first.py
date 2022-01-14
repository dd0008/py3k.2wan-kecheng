# 编译人：d
# 编译时间：,
#可以输出表达式
print(1+3)

#可以输出数字
print(5)

#可以输出字符串
print("hello")

#可以输出到文件
fp=open("F:/TEXE.txt","a+") #指定盘符必须存在；fp是自定义的名字；a+意指若有这个文件则打开文件后接着写入，若没有则新建再写入
print('helloworld',file=fp)#使用file=
fp.close()#关闭fp这个文件

a=open('f:/text.doc','a+')
print('hello,a',file=a)
a.close()

b=open('f:/text.xls','a+')
print('hello,b',file=b)
b.close()

#输出到一行
print('hello','a','b')