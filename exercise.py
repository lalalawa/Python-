# coding:utf-8

invite_list = ['a', 'b', 'c']
print(invite_list)
print('这位嘉宾无法去', invite_list[2])
invite_list.pop()
# append在列表的末尾添加一个元素，会直接修改原列表，返回值是none
invite_list.append('d')  # 不需要赋值，直接添加元素就行
print(f'新的邀请名单为{invite_list}')
invite_list.insert(0, 'e')
invite_list.insert(2, 'f')
print(f'我想邀请的人是{invite_list}')
poped_list = []  # 将不邀请的单独放一个空列表，便于后续添加新的值
while len(invite_list) > 2:
    poped = invite_list.pop()
    poped_list.append(poped)
for name in poped_list:
    print(name.title()+" Sorry,I can't have dinner with you")
for name in invite_list:
    print(name.title()+" I'm happy to invite you to have dinner with me")

#
sandwich_orders = ['san', 'ming', 'zhi']
finished_sanwiches = []
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print("I made your "+sandwich_order)
    finished_sanwiches.append(sandwich_order)
print(finished_sanwiches)
print("I made all the sandwiches")

#
print("The pastramu has been sold out")
sandwich_orders = ['san', 'astramu', 'ming', 'zhi', 'astramu', 'astramu']
finished_sanwiches = []
removed_sandwiches = []
print(sandwich_orders)
while 'astramu' in sandwich_orders:
    sandwich_order = sandwich_orders.remove('astramu')
    # list.remove()返回值不是移除的元素，而是NONE
    finished_sanwiches.append(sandwich_order)  # 此时全是None
    removed_sandwiches.append('astramu')
# print("finished_sanwiches:"+str(finished_sanwiches))，格式错误，python中，+不可以连接字符串和列表
print(f"finished_sanwiches:{finished_sanwiches}")
print(f"sandwich_orders:{sandwich_orders}")
print(f"removed_sandwiches:{removed_sandwiches}")
# 采用print(f"")进行格式化的输出，用{}括起来，表示要替换的内容，在双引号里面


#
dream_places = {}
sign = True
while sign:
    name = input("please enter your name:")
    place = input(
        "if you could visit one place in the world,where would you go?")
    dream_places[name] = place
    sign1 = input("do you want to continue,enter(yes/no)")
    if sign1 == 'no':
        sign = False
print(dream_places)

#
destinations = []
while True:
    prompt = 'if you could visit one place in the world, where would you go?'
    prompt += "\n(enter 'quit' to end the survey.)"
    response = input(prompt)
    if response == 'quit':
        break
    else:
        destinations.append(response)
print('survey result')
for destination in destinations:
    print(f'{destination} is a dream vacation spot for someone.')
