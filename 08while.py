# coding:utf-8

# for循环用于针对集合中的每个元素的一个代码块，而while循环不断运行，直到满足条件为止
# 使用while时，要避免无限循环
current_number = 1
sum = 0
while current_number <= 5:
    sum = sum+current_number
    current_number += 1
print(sum)

# 定义一个退出值
prompt = '\nTell me something,and I will repeat it back to you:'
prompt += "\n Enter 'quit' to end the program:"
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# 使用break退出循环
prompt = '\nPlease enter the name of a city youu have visited'
prompt += "\n Enter 'quit' to end the program:"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd like to go to:"+city.title())

# 在循环当中使用continue，返回到循环开头，并根据条件测试结果决定是否要继续执行循环
# 计算1-10中的奇数的和
current_number = 1
sum = 0
while current_number <= 10:
    if current_number % 2 != 0:
        sum += current_number
        current_number += 1
    elif current_number % 2 == 0:
        current_number += 1
        continue
print(sum)

# 使用while循环来处理列表和字典
# for循环也可以遍历列表，但是在for循环当中不应该修改列表，否则难以跟踪列表的元素
# 使用while循环能够在遍历列表的同时对列表进行修改
# 将while循环同列表和字典结合起来使用，能够收集、存储并组织大量输入，供以后查看和显示

# 在列表之间移动元素
# 已经有一个包含新注册但还未验证的网站用户，验证这些用户后，将他们移动到另一个已经验证的用户列表当中
unconfirmed_users = ['alice', 'lucy', 'brain']
confirmed_users = []  # 创建一个新的列表便于存储已经验证过的用户
while unconfirmed_users:  # 直接
    current_user = unconfirmed_users.pop()  # 利用pop从列表的末尾删除未验证的用户
    print("Verifying users:"+current_user.title())
    confirmed_users.append(current_user)  # 移除没有验证的列表，再添加到新的列表
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#删除包含特定值的所有列表元素
#函数remove()删除特定列表的值，只能删除一个，重复的没有办法
#删除列表中所有包含特定值的元素，可以不断运行while
pet=['dog','cat','dog','cat','pig','cat']
print(pet)
while 'cat' in pet:
    pet.remove('cat')
print(pet)

#使用用户输入来填充字典
responses={}
polling_active=True
while polling_active:
    name=input("\nWhat is your name:")
    response=input("\nWhich mountain would you like to climb someday?")
    responses[name]=response#将用户输入的信息存储在字典当中
    repeat=input("Would you like to let another person respond?(yes/no)")
    if repeat=='no':
        polling_active=False
print('\n---Poll Results---')
for name,response in responses.items():
    print(name+" would like to climb "+response+'.')