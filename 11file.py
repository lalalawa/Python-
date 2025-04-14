# coding:utf-8

"""
Python要在当前执行的文件所在目录中查找指定的文件,否则就要给出该文件的完整路径
"""
# 读取整个文件
# 读取文本文件时，python将其中所有的文本都解读为字符串，若读取的数字，要将其作为数值使用，就必须使用函数int()将其转换为整数，或者使用函数float()将其转化为浮点数
import json
with open('pi_digits.txt') as file_object:  # 函数open()返回一个表示文件的对象，with在不再需要访问文件后将其关闭
    contents = file_object.read()
    print(contents)
# 若文件的末尾有多余的空行，可在print语句中使用rstrip():
file_path = 'C:/Users/32826/Desktop/text_file1.txt'
with open(file_path) as file_object:  # 函数open()返回一个表示文件的对象，with在不再需要访问文件后将其关闭
    contents = file_object.read()
    print(contents.rstrip())
# 因为在python中反斜杠\作为转义字符，在表示绝对路径时，最好避免这种写法
# 可以采用以下几种方法避免
# r'C:\Users\32826\Desktop\text_file1.txt'在字符串前面加上 r 表示这是一个原始字符串
# 'C:\\Users\\32826\\Desktop\\text_file1.txt'将每个反斜杠都写成双反斜杠 \\，这样其中一个反斜杠会转义另一个反斜杠
# 'C:/Users/32826/Desktop/text_file1.txt':在 Windows 系统中，路径也可以使用正斜杠 / 来表示，这在 Python 中同样有效。

# 读取文件，要么将数据文件存储在程序文件所在的目录，要么将其存储在程序文件所在目录下的一个文件夹中

# 逐行读取：在文件中查找特定信息或修改文件中的文本
# 以每次一行的方式检查文件，可对文件对象使用for循环：
# 循环遍历文件中的每一行
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())  # 利用rstrip可以去除字符串末尾的空白字符
# 将文件pi_digits.txt的各行存储在了一个列表之中，该列表被存储在lines中
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
# readline和readlines的区别：
# readline--每次读取一行的内容，readlines--一次性读取文件的内容，并且按行返回list

# 使用文件的内容
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()  # 将各行都加入到pi_string，并删除每行末尾的换行符
    print(pi_string)
    print(len(pi_string))

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ''
for line in lines:
    pi_string += line.strip()  # strip()删除字符串两端的空白格，rstrip()仅删除字符串末尾的空白格
print(pi_string)
print(len(pi_string))

# 当文本内容很长，只需要显示部分内容时，
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ' '
for line in lines:
    pi_string += line.strip()
print(pi_string[:52]+'...')
print(len(pi_string))

# 圆周率值中是否包含我的生日
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ' '
for line in lines:
    pi_string += line.strip()
birthday = str(20020512)
if birthday in pi_string:
    print("Your birtheday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi")

# 写入空文件
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
# 以写入模式打开文件时，可以指定'r'只读模式,'w'写入模式,'a'附加模式,'r+'读取和写入文件的模式
# r：读取模式，需要文件存在，若不存在，则会发生报错
# w:写入模式，若文件已经存在且有其余内容，会将原内容替换为新写入的内容，若文件不存在，则会自动创建文件并写入
# rb,wb:二进制下的读和写模式，因为图片或音频等内容都是二进制的，因此可以用这两个参数进行读或写
# python只能将字符串写入文本文件，要将数值数据存储到文本文件中，必须要先使用函数str()将其转换为字符串的格式，即数值类的数据要转换为字符串的类型

# 写入多行
# 函数wrote()并不会在写入的文本末尾添加换行符，故要想写入多行数据需要指定换行符
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming\n")
    file_object.write("I love creating new games")

# 若不覆盖文件原有的内容，而是给文件添加内容，可以利用附加模式打开文件
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("\nI have to work hard")

# python利用被称为异常的特殊对象来管理程序执行期间发生的错误，每当发生错误时，python都会创建一个异常的对象
# 异常使用try-except代码块让Python执行指定的操作，同时告诉Python发生异常时应如何操作
# 只有可能引发异常的代码才需要放在try语句中,当try大麦快成功执行时才需要运行的代码应放在else代码块中

# 处理ZeroDivisionError异常
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
# 如果try代码块中的代码运行起来没有问题，python将跳过except代码块；若try块中的代码导致了错误，Python将查找except代码块，并运行其中的代码

# 使用异常避免崩溃：希望程序能够妥善处理无效的输入，并能再提示用户提供有效输入，而不至于崩溃
# 创建一个只运行除法的简单计算器
print("Give me two numbers,and I'll divide them")
print("Enter 'q' to quit")
while True:
    first_number = input("First number:")
    if first_number == 'q':
        break
    second_number = input("\nSecond number:")
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

# 处理FileNotFoundError异常
# 当使用文件时，找不到文件，文件名不正确，或该文件不存在
filename = 'Lichee.txt'
try:
    with open(filename, encoding='utf-8') as f_object:
        contents = f_object.read()
except FileNotFoundError:
    print(f"Sorry,the file {filename} does not exit")

# 分析文本
# split()函数，根据一个字符串创建一个单词列表,以空格为分隔符将字符串拆分成多个部分，并将这些部分都存储到一个列表之中
title = "Alice in Wonderland"
print(title.split())

filename = 'Alice.txt'
try:
    with open(filename, encoding='utf-8') as file_object:  # 文件操作时要明确指定文件的编码，才能避免掉编码错误
        contents = file_object.read()
except FileNotFoundError:
    msg = f"Sorry,the file {filename} does not exit"
    print(msg)
else:
    # 计算文件大致包含了多少个单词
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

# 存储数据，利用json来存储数据
# 模块json能够将简单的Python数据结构转储到文件中，并在程序再次运行时加载该文件的数据
# json数据格式并非是python专用，json模块是用于处理JSON数据的标准库

# 使用json.dump()和json.load()
# 函数json.dump()接受两个实参：要存储的数据以及可用于存储数据的文件对象
numbers = [2, 3, 5, 7, 13]
filename = 'numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)

# 使用json.load()将该列表读取到内容之中
with open(filename) as f_object:
    numbers = json.load(f_object)
print(numbers)
# 保存和读取用户生成的数据
username = input("What's your name?")
filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)  # 调用json.dump(),并将用户名和一个文件对象传递过去，从而将用户名存储在文件之中
    print(f"We'll remember you when you come back,{username}!")

#向被存储的名字表示问候
with open(filename) as f_obj:
    username=json.load(f_obj)
    print(f"Welcome back,{username}!")
