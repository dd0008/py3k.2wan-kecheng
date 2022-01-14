# 开发人：d
# 开发时间：2021/12/21,15:51

def cunt_char(text,char): #定义一个函数。将计数代码定义为一个函数的好处是他可以多次调用，多次运行
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count # return在for循环之外

filename = input('Enter a filename:') #需输入全路径文件名，比如 C:/Users/D/Desktop/2.txt
with open(filename) as f: #无论期间是否抛出异常，都能保证 with as 语句执行完毕后自动关闭已经打开的文件
    text = f.read() #.read()读取，类似的有.upper()，.lower()
print('‘e’在文件中出现了:',cunt_char(text,'e'),'次')
# print('‘/’在文件中出现了:',cunt_char(text,'/'),'次')

for char in 'abcdef':
    perc = 100 * cunt_char(text,char) / len(text)
    #每遍历一个字母的时候，引用函数统计一下这个字母在文件中的次数。再除以文件中所有字符的总长度
    print('{0} - {1}%'.format(char,round(perc,2)))
    #round用于保留小数位数;format格式化字符串，指定char与perc位置，并加%






