# coding:utf-8

names = ['lawa', 'vivi', 'wang', 'luo']
for name in names:
    if name == 'vivi':
        print(name.upper())
    else:
        print(name.title())

# 使用and或者or可以检查多个条件

# 检查特定的值是否包含在列表当中(关键字in判断特定的值是否包含在列表当中)
names = ['lawa', 'vivi', 'wang', 'luo']
if 'lawa' in names:
    print("True")

# 检查特定值是否不包含在列表当中：使用关键字not in
banned_users = ['lawa', 'vivi', 'wang']
user = 'shuang'
if user not in banned_users:
    print(user.title()+" you can come to the meeting")

# 布尔值通常用于记录条件，游戏是否正在运行，用户能否编辑网站的特定内容（True ||False）

# if的语法
# if conditional_test:
#   do something

age = input("请输入你的年龄大小：")
age = int(age)
if age <= 4:
    print('你满足免费的条件')
elif age >= 18:
    print('你需要缴纳10美元')
else:
    print("你需要缴纳五美元")
# 第二种更加简洁的写法
age = input('请输入你的年龄大小：')
age = int(age)
price = 0
if age < 4:
    price = 0
elif age >= 18:
    price = 10
else:
    price = 5
# 打印输出需要将数值转换为字符输出,使用 + 运算符去连接字符串和整数Python 无法处理
print("你需要给的门票是："+str(price)+'元')
print(f"你需要给的门票是：{price}元")  # 第二种输出格式，便于字符串的转化
print("你需要给的门票是：{}元".format(price))  # {}为一个占位符，会将format.()括号内的内容插入到占位符中

# format
# string.format(arg1, arg2, ...),string 是包含占位符的字符串，arg1, arg2, ... 是要插入到字符串中的参数
# 使用位置参数来填充占位符。占位符中的数字表示要插入的参数的索引，索引从 0 开始。
message = "我叫 {}，今年 {} 岁。".format("张三", 25)
print(message)
# 利用关键字参数填充占位符，在占位符中指定关键字，然后在 format() 方法中使用关键字参数传递值。
# 示例代码
message = "我叫 {name}，今年 {age} 岁。".format(name="李四", age=30)
print(message)
# format() 方法还支持在占位符中使用格式化选项，用于指定参数的显示格式,格式化选项通过冒号 : 后面的格式说明符来指定
# 保留两位小数
pi = 3.1415926
message = "圆周率约为 {:.2f}".format(pi)  # {:.2f} 表示将参数格式化为浮点数，并保留两位小数
print(message)

# 千位分隔符
number = 1234567
message = "数字是 {:,}".format(number)  # {:,} 表示在数字中添加千位分隔符
print(message)
# 左对齐
text = "Hello"
message = "{:<10}".format(text)
print("|{}|".format(message))

# 右对齐
message = "{:>10}".format(text)
print("|{}|".format(message))

# 居中对齐
message = "{:^10}".format(text)
print("|{}|".format(message))
# < 表示左对齐，> 表示右对齐，^ 表示居中对齐，数字 10 表示总宽度

# python中，{}用于创建字典或者集合的符号，而:用于分割键和值，用于创建字典、字典推导式以及格式化字符串
# python并不要求if-elif结构后面必须要有else的代码块，else可以省略
# 也不是所有的情况都需要使用if-else或者if-elif的结构，当需要测试所有条件是否都满足，应该直接应用if的简单句
name_list = ['lawa', 'vivi', 'shuang']
if 'lawa' in name_list:
    print('welcome'+' lawa')
if 'wang' in name_list:
    print('welcome wang')
if 'vivi' in name_list:
    print('welcome vivi')

name_lists = ['lawa', 'vivi', 'shuang']
for name_list in name_lists:
    if name_list == 'vivi':
        print('sorry,vivi is not here')
    else:
        print(f'welcome {name_list}')

# 在运行for循环前需要确定列表是否为空
name_lists = []
if name_lists:
    for name_list in name_lists:
        print('welcome'+name_list)
else:
    print("Sorry,I don't know who you want")

# 使用多个列表，
available_toppings = ['mushrooms', 'olivers', 'green peppers',
                      'pineaoole', 'extra cheese']  # 当这个是固定的，也可以采用元组进行定义
requested_toppings = ['mushrooms', 'french frices', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding '+requested_topping)
    else:
        print("sorry,we don't have "+requested_topping)
print('finished')
