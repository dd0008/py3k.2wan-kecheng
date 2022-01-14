# 开发人：d
# 开发时间：2021/12/20,14:09


ap = open('E:/试一试/只读.txt') #没有参数，默认只读
con = ap.read() #读取
print(con) #显示读取的内容。
ap.close()

ap = open('E:/试一试/只读.txt')
print(ap.read(3)) #显示读取的内容。
print(ap.read(1)) #显示读取的内容。
print(ap.read(1)) #显示读取的内容。
ap.close()

ap = open('E:/试一试/只读.txt')
ap.read() #读取完成
print('Re-reading')
print(ap.read()) #再次读取，返回为空字符串。
print('Finished')
ap.close()

ap =open('E:/试一试/只读.txt')
print(len(ap.read()))
ap.close()

ap = open('E:/试一试/只读.txt')
print(ap.readlines())
ap.close()

ap = open('E:/试一试/只读.txt')
for j in ap: #j随机取的变量名，在文件中指代行。
    print(j) #用for循环来逐行打印
ap.close()

print(len(open('E:/试一试/只读.txt').readlines())) #这里len()返回的是行数。

try:
    f = open('E:/试一试/只读.txt')
    print(f.read())
finally:
    f.close() #文件使用完关闭是个好习惯，file.close通常和try/finally结合使用。


try: #先执行try block
    with open("E:/试一试/只读.txt") as f:#无论期间是否抛出异常，都能保证 with as 语句执行完毕后自动关闭已经打开的文件
        print(f.read())
except: #发现异常则执行except block，无异常则不执行。
    print('Error')


with open("E:/试一试/只读.txt") as f: #with下的代码行缩进，用with打开的文件执行完会自动关闭，代替file.close
    print(f.read())

#文本分析器之打开读取文件
filename = input('Enter a filename:') #需输入全路径文件名，比如C:/Users/D/Desktop/2.txt
with open(filename) as f: #无论期间是否抛出异常，都能保证 with as 语句执行完毕后自动关闭已经打开的文件
    text = f.read() #.read()读取，类似的有.upper()，.lower()
print(text)

