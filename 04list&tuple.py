# coding=utf-8

# list表示列表，是一种有序的集合，能够随时添加并删除其中的某些元素
classmates = ['Michael', 'Bob', 'Tracy']
print("初始列表:", classmates)  # 输出初始列表,python会将列表中的所有内容打印出来，包括方括号

print("列表长度:", len(classmates))
print("第一个元素:", classmates[0])  # 利用索引来访问list当中每一个位置的元素，是利用[]+数字来表示
# 获取列表元素时，python只会返回该元素，不会返回方括号和引号

# 索引不可以越界
# 在不知道列表长度的情况下，获取最后一个元素，可以直接利用-1作为索引
# 但是在列表为空的时候，访问最后一个元素的方式会出错
print("最后一个元素:", classmates[-1])  # 表示倒数第一个
print("倒数第三个元素:", classmates[-3])  # 表示倒数第三个

# list是一个可变的有序表，能够往list当中追加元素到末尾当中
# append()在列表的末尾添加元素，可以创建一个空列表再根据一系列的append向列表中添加元素
# 把一个指定的元素添加到列表的末尾,让列表的长度增加1，主要用法list_name.append(element)
classmates.append('Adam')
print("追加元素后:", classmates)

# insert()插入元素
classmates.insert(1, 'Jack')  # 将元素插入到指定的位置
print("插入元素后:", classmates)

# pop()删除列表末尾的元素，并能够接着使用他
print("删除末尾元素:", classmates.pop())  # 删除list末尾的元素
print("删除末尾元素后:", classmates)
# pop()也可以用来删除列表中任何位置的元素，需要在括号中指定要删除的元素的索引即可
print("删除指定位置元素:", classmates.pop(1))  # 删除list指定位置的元素
print("删除指定位置元素后:", classmates)

# 知道删除元素在列表中的具体位置，可以用del语句进行删除，del能够删除任何位置处的列表元素，只要知道索引即可
classmates = ['Michael', 'Bob', 'Tracy']
del classmates[0]
# 当删除一个元素后续不会再用到，就用del的语句，如果后续会用到要删除的这个元素就用pop()函数

classmates[1] = 'Lucy'  # 将某个元素替换成别的元素
print("替换元素后:", classmates)

L = ['Apple', 123, True]  # list当中各个元素的类型可以不同
print("包含不同类型元素的列表:", L)

s = ['python', 123, ['asp', 'lawa'], 'scheme']  # list元素中也可以包含另外一个list
print("包含子列表的列表:", s)
print("包含子列表的列表长度:", len(s))

# 这种包含关系能够拆开写
p = ['asp', 'lawa']
s = ['python', 123, p, 'scheme']
print("拆开定义的包含子列表的列表:", s)

# 空的list，长度为0
L = []
print("空列表长度:", len(L))

# 当不知道要从列表中所删除值的位置，只知道元素值的时候，可以使用remove()函数
# remove()函数只删除了第一个指定的值，若删除的值在列表中出现了很多次，就需要利用循环判断是否删除了所有这样的值
classmates = ['Michael', 'Bob', 'Tracy']
classmates.remove('Bob')  # 删除第一个出现的Bob
print(classmates)  # 此时已经将Bob删除

# 使用sort()可以对列表进行永久性的排序
name = ['lawa', 'vivi', 'chizi']
name.sort()  # 此时按照字母顺序进行排列
print(name)
name = ['lawa', 'vivi', 'chizi']
name.sort(reverse=True)  # 向sort()方法传递参数，reverse=True,此时会按照相反的顺序进行排列
print(name)
# 使用sorted()能够对列表进行临时性的排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('原始列表为：')
print(cars)
print('\n进行排序后的列表为:')
print(sorted(cars))  # 也是按照字母的顺序对列表进行排序
print(f'看原始的列表是否发生了改变\n{cars}')
# 利用reverse()函数可以反转元素的排列顺序
cars.reverse()  # reverse也是永久性地修改列表元素的排列顺序，但再调用依次reverse便能够恢复到原顺序
print(f'按照相反的顺序输出：\n{cars}')

# tuple也是一种有序列表，但是tuple一旦进行了初始化便不能够进行修改
classmates = ('Lawa', 'Jack', 'Zhou')
print("初始元组:", classmates)
print("元组第一个元素:", classmates[0])
print("元组最后一个元素:", classmates[-1])

# 空的tuple
t = ()
print("空元组:", t)

# 只有一个元素的tuple定义时必须要加一个,
t = (1,)
print("只有一个元素的元组:", t)

t = ('a', 'b', ['A', 'B'])
print("包含列表的元组:", t)
t[2][0] = 'X'
t[2][1] = 'Y'
print("修改包含列表的元组后:", t)

# list使用[]，tuple采用（）

L = [['Apple', 'Google', 'Miscrosoft'], ['Java', 'Python', 'Ruby', 'PHP'],
     ['Adam', 'Bart', 'Bob']
     ]
print(L[0][0])
print(L[1][1])
print(L[2][2])
