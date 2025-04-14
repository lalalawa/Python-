#coding=utf-8

print('I\'m \"ok\"')
print('I\'m learning\nPython.')
print('\\\n\\')#\\的意思表示的就是\，因为转义字符转义掉了
print('\\\t\\')
print(r'\\\t\\')#python里允许使用r''表示''里面的内容默认不发生转义
text = """
line1
line2
line3
""".strip()#利用strip() 方法去掉了字符串开头和结尾的空白字符
print(text)
print(r'''hello,\n'
'world''')#前面加上r表示默认（）内的内容不发生转义
age=int(input('请输入年龄的大小'))#input()函数返回的是字符串的类型
if age>=18:
    print('adult')
else:
    print('teenager')

print(10/3)#使用/除，这种除法的计算结果是浮点数，即做精确的计算
print(10//3)#使用//进行除，这种除法是进行取整，只取结果的整数部分
print(10%3)#利用%进行取余运算

print('n=123')
print('f=456.789')
print('s1=Hello,world')
print('s2=Hello,\\\'Adam\\\"')
print('s3=r\'Hello,\"Bart\"')
print('s4=r\'\'\'Hello,')
print('Bob!\'\'')
#print函数可以使用,（逗号）对字符串进行拼接
#UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，
# 常用的英文字母被编码成1个字节，汉字通常是3个字节，
# 只有很生僻的字符才会被编码成4-6个字节。
# 如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间
#ASCII编码实际上可以被看成是UTF-8编码的一部分
print('包含中文的dtr')
ord('A')#利用ord()函数能够获取单个字符的编码，即获取字符的整数表示
ord('中')
chr(65)
chr(25991)#chr()函数能够将编码转换为对应的字符
'\u4e2d\u6587'#知道十六进制将编码转换为字符
#python当中的字符串类型是str，在内存当中以unicode进行表示，一个字符对应了若干个字节
#将str变为以字节为单位的btes，便于在网络上进行传输，或者方便保存在磁盘上
x=b'ABC'#python对bytes类型的数据用带b前缀的单引号或双引号表示，bytes的每个字符都只占用一个字节
'ABC'.encode('ascii')#利用encode()函数能够将str指定为bytes
'中文'.encode('utf-8')

#纯英文的str可以通过ascii编码为bytes,中文能够利用ut-8，但是含有中文的str无法利用ASCII进行编码，会出错

#使用decode()能够将获取到的bytes变为str
b'ABC'.decode('ascii')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

#当bytes当中含有一部分无效的字节时，利用errors=ignore忽略错误的细节
b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore')
#len()函数计算str字符当中的字符数，若是bytes，则是计算字节数
len(b'ABC')
len(b'\xe4\xb8\xad\xe6\x96\x87')
len('中文'.encode('utf-8'))
#一般1个中文字符占用3个字节，而1个英文字符只占用一个字节


#当自己的源代码包含了中文时，保存源代码时，务必指定保存为UTF-8的编码
#!/usr/bin/env python3      （这句话说明是一个python的可执行程序）
# -*- coding: utf-8 -*-     （这句话说明必须要按照UTF-8编码读取源代码，否则中文的输出会含有乱码）

'Hi,%s,you have $%d.'%('Lisa',1000000)#这里面单独的%起到了连接格式化字符和需要的内容
print('%2d-%.2f'%(3,1.456278))#还能够指定是否补0和整数与小数的位数
#%s会将任何的数据类型转化为字符串
'Age:%s.Gender%s'%(25,True)
#利用%%表述%这个字符

#使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……
'Hello,{0},成绩提升了{1:.1f}%'.format('小明',17.1225)#，{1:.1f}把format传入的第二个参数格式化为保留小数点后1位的浮点数，最终得到17.1
#python中{}用于标记占位符，1：这是索引值，它指定了要从 format 方法传入的参数中选取第几个参数进行格式化。
#:：它是格式化指令的起始符号，用于分隔索引和具体的格式化规则。
#.1f：这是精度控制部分，1 表示保留小数点后 1 位,f表示格式化的类型为浮点数
#str.format() 方法里，除了花括号 {} 内的内容会被当作占位符和格式化指令处理外，其他普通字符都会被原样输出。

#print(f"") 用于输出格式化字符串，允许在字符串中嵌入变量或表达式 ,变量需要放在大括号内                           
r=2.15
s=3.14*r**2
print(f'The area of a circle with radius {r} is{s:.2f}')
#{r}被变量r的值替换，{s:.2f}被变量s的值替换，并且:后面的.2f指定了格式化参数（即保留两位小数）

s1=72
s2=85
r=(s2-s1)*100/s1
print('小明的成绩从去年的{0}分提升到了今年的{1}分，共提升了百分之{2:.2f}%'.format(s1,s2,r))
print(f'小明的成绩由去年的{s1}分提升到了今年的{s2}分，共提升了百分之{r:.2f}%')


#python当中字符串的拼接，利用+号来合并字符串
first_name="ada"
last_name="lover"
full_name=first_name+" "+last_name
print(full_name)

#rstrip()#用于删除字符末尾中的多余空格，但只有调用这个命令的时候才会删除多余空白值，变量本身的大小不会发生变化
favorite_language='python '
print(favorite_language)
favorite_language.rstrip()
favorite_language=favorite_language.rstrip()#只有这样赋值之后才能够将变量中末尾的空白值删去
print(favorite_language)

#lstrip()删除字符串开头的空白
favorite_language=' python ' 
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
#strip()删除字符串两端的空白


#在编写字符串时，注意引号匹配的问题，何时用'',何时用“”