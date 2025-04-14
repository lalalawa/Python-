
# coding=utf-8
# print会依次打印每个字符串，遇到,会显示输出一个空格
print('The quick brown fox', 'jump over', 'the lazy dog')
print('100 +200 =', 100+200)
name = input('please enter your name')
print('Hello', name)
print('1024*768=', 1024*768)

name = 'ad loVE'
print(name.title())  # 函数title（）将每个单词的首字母都改为大写
print(name.upper())  # 函数upper()将所有的字母变为大写
print(name.lower())  # 函数lower()将所有的字母都变为小写

print('\tpython')  # 制表符
print('python')
print("Languages:\n\tPython\n\tC\n\tJavascript")  # 使输出的结构好看

famous_man = 'albert einstein'
quote = '"A person who never made a mistake never tried anything new."'
sentence = famous_man.title()+' said,'+quote
print(sentence)

# str()函数：将非字符串的值表示为字符串
age = 23
message = 'Happy'+str(age)+'rd birthday'
print(message)


# 使用input()函数时，应该指定清晰而易于明白的提示，准确地指出希望用户提供的信息
name = input("Please enter your name:")
print("Hello "+name)
# 当输入的提示超过一行时，可以将提示存储在一个变量当中，再将该变量传递给函数input()
promt = "If you tell us who you are,we can personalize the messages you see."
promt += "\n What's your name?"
name = input(promt)
print("Hello "+name)

# int()将数字的字符串转换为数值进行表示
height = input('How tall are you?')
height = int(height)
if height >= 180:
    print("Wow,you are tall enough")
else:
    print("You need to be taller")

# 求模运算，将两数相除并返回余数，只会指出余数的大小
number = input("Enter a number")
number = int(number)
if number % 2 == 0:
    print(str(number)+" is even")
else:
    print(str(number)+" is odd")
