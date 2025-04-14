# coding:utf-8

# 简单的字典
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
# 上述字典alien_0存储了外星人的颜色和点数，使用print访问并打印这些信息
# 和列表不同，字典是key-value的存储和访问的方式，访问字典的元素要使用dict[key]的方式
# 字典中，每一个键都与一个值相关联，dict用放在{}中的一系列键值对来表示，键和值用冒号分隔，key-value之间利用，(逗号)进行分割
# 最简单的字典只有一个键值对

# 访问字典中的值
alien_0 = {'color': 'green', 'points': 5}
new_point = alien_0['points']
print('you have just won '+str(new_point)+' points!')

# 添加键-值对，字典是一种动态的结构，能够随时在其中添加键-值对
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25  # 距离屏幕顶部25像素的地方
print(alien_0)
# 字典并不关心排列顺序，只关心key-value之间的关系

# 创建空字典
alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 10
print(alien_1)

# 修改字典中的值
alien_1['color'] = 'yellow'
print(alien_1)
# 对一个以不同速度移动的外星人的位置进行跟踪，先存储该外星人的当前速度，并据此确定该外星人将向右移动多远
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x_position:"+str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
    # 新的位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position']+x_increment
print('New x-position:'+str(alien_0['x_position']))

# 删除键-值对(key-value)
# 对字典当中不在需要的信息，可以使用del语句将相应的key-value对彻底删除。必须要指明字典名以及要删除的键
# del语句删除key-value对是永久性消失的，但是可以重新创建一个具有相同键的新key-value对
del alien_0['speed']
print(alien_0)
alien_0['speed'] = 5
print(alien_0)

# 由类似对象组成的字典
# 可以利用字典存储众多对象的同一种信息
favorite_languages = {
    'vivi': 'python',
    'lawa': 'c',
    'wang': 'Java',
    'luo': 'c',
}
print(favorite_languages)
print("vivi's favorite language is:"+favorite_languages['vivi'].title())

# 遍历字典
# 一个python字典可能只含有几个键-值对，也可能含有数百万个键-值对

# 遍历所有的键-值对
user_0 = {
    'username': 'lawa',
    'age': 22,
    'gender': 'female',
}
for key, value in user_0.items():
    print("\nKey:"+key)
    print("Value:"+str(value))

for name, language in favorite_languages.items():
    print(name.title()+" 's favorite language is "+language.title())
# items是字典对象的一个内置方法，能够遍历字典中的键值对

# 遍历字典中的所有键
# 不需要使用字典中的值时，利用keys(),会返回一个包含字典所有键的视图对象
# 遍历字典时，会默认遍历所有的键
friends = ['lawa', 'wang']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi "+name.title()+" I see your favorite language is " +
              favorite_languages[name].title())
        # favorite_languages[name]利用键name去访问了字典当中对应的值，在字典中可以通过键去访问对应的值

# 按顺序遍历字典中的所有键
# 在for循环中对返回的键进行排序，利用函数sorted()获得按特定顺序排列的键列表的副本：
# sorted(iterable, key=None, reverse=False)
# iterable：这是必需参数，代表要排序的可迭代对象，比如列表、元组、字符串等。
# key：这是可选参数，是一个函数，它会作用于可迭代对象中的每个元素，排序时会依据这个函数的返回值来进行。默认值为 None，也就是直接比较元素本身。
# reverse：这也是可选参数，是一个布尔值。若设置为 True，则按降序排序；若为 False（默认值），则按升序排序。
words = ["apple", "banana", "cherry", "date"]
# 按字符串长度排序
sorted_words = sorted(words, key=len)
print(sorted_words)  # 输出: ['date', 'apple', 'banana', 'cherry']

for name in sorted(favorite_languages.keys()):
    print(name.title())

# 遍历字典中的所有值
# values()返回一个值列表，不包含任何的键
for language in favorite_languages.values():
    print(language.title())
# 但是该方法提取了字典当中所有的值，没有考虑到是否重复的问题，要剔除重复的项，采用集合set
# 集合set类似于列表，但每个元素都是独一无二的
for language in set(favorite_languages.values()):
    print(language.title())

# 嵌套：将一系列字典存储在列表中，或将列表作为值存储在字典当中
# 字典列表
alien_2 = {'color': 'blue', 'points:': 9}
aliens = [alien_0, alien_1, alien_2]  # 将字典放入到列表当中
for alien in aliens:
    print(alien)

# 利用代码自动生成
aliens = []
for alien_number in range(0, 30):
    new_alien = {'color': 'black'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("....")
print("total number="+str(len(aliens)))

aliens_1 = []
for alien_number in range(0, 30):
    new_alien = {'color': 'pink', 'points': 6, 'speed': 20}
    aliens_1.append(new_alien)
for alien in aliens_1[0:3]:
    if alien['color'] == 'pink':
        alien['color'] = 'green'
        alien['speed'] = 15
for alien in aliens_1[:5]:
    print(alien)
print("....")

# 在字典当中存储列表
# 当需要在字典当中将一个关键键关联到多个值时，都可以在字典中嵌套一个列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print("Your odder "+pizza['crust']+"-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)
favorite_languages = {
    'vivi': ['python', 'java'],
    'lawa': ['c', 'ruby'],
    'wang': ['Java', 'R'],
    'luo': ['c', 'hah'],
}
for name, languages in favorite_languages.items():
    print("\n"+name.title()+" 's favorite languages are:")
    for language in languages:
        print("\t"+language.title())

# 在字典中存储字典
users = {
    'lawa': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'vivi': {
        'first': 'nlbert',
        'last': 'finstein',
        'location': 'cminceton'
    }
}
for user_name, user_info in users.items():
    print("\nusername:"+user_name)
    full_name = user_info['first']+' '+user_info['last']
    location = user_info['location']
    print("\tFull name:"+full_name)
    print("\tLocation:"+location)
