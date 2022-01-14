# 开发人：d
# 开发时间：2021/12/20,15:35

myfile = open("E:/试一试/1.txt",'w') #'w'将已有内容清除之后写入，‘a+'在已有内容后接着写入。当然若文件不存在就创建。
#print('haode1',file=myfile)
myfile.write('ni hao a')
myfile.close()

myfile = open("E:/试一试/1.txt",'r')
print(myfile.read())
myfile.close()

msg = 'hello world!'
file = open("E:/试一试/1.txt",'w')
am = file.write(msg) #写入的字节数。file.write(msg)==len(msg)
print(am)
file.close()

