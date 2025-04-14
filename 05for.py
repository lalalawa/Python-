#coding:utf-8

#利用for循环可以遍历所有的列表
#for xx in yy:xx的值是临时的变量，可以随便定义，xx可以是任意合法的变量名
magicians=['lawa','vivi','wang']
for magician in magicians:
    print(magician)
#for语句末尾的冒号：说明下一行是循环的第一行
#xx相当于是临时存储变量的名称，主要选择描述单个列表元素的有意义的名称
#每个缩进的代码都是循环的一部分，for循环后面没有缩进的代码都只执行依次，不会重复执行
for magician in magicians:
    print(magician.title()+",that's was a great trick!")#利用+将所有进行拼接
    print("I can't wait to see you next trick,"+magician.title()+".\n")
print("Thank you everyone!")
#需要正确使用缩进，避免出现不必要的缩进，忘记缩进

#range():从指定的第一个值开始数，并在达到指定的第二个值后停止，因此该输出不包含5
for value in range(1,5):
    print(value)

#利用函数list()能够将range()里的结果直接转换为列表
numbers=list(range(1,6))
print(numbers)
#range()还可以指定步长
even_numbers=list(range(2,11,2))#从2开始数然后不断的加2  range(start,end-1,step)
print(even_numbers)

#将1~10个数的平方加入到一个列表当中
squares=[]
for value in range(1,11):
    value=value**2
    squares.append(value)
print(squares)
#第2种更加简洁的写法
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

#对数字列表进行统计计算的函数:sum,min,max
digits=[1,2,3,4,5,6]
print(min(digits))
print(max(digits))
print(sum(digits))

#列表解析将for循环和创建新元素的代码合并成一行，并自动附加上新的元素,简化代码
squares=[value**2 for value in range(1,11)]#先指定一个描述性的列表名，再定义一个表达式，生成要存储在列表中的值，此时用for末尾不需要：
print(squares)

number=[value for value in range(1,21)]
print(number)
number_sum = sum(range(1, 1000001))
print(number_sum)

odd_number=[]
for value in range(1,21):
    if value%2!=0:
        odd_number.append(value)
print(odd_number)

#法2
odd_number=range(1,21,2)
for i in odd_number:
    print(i)

#切片,list [start:end] 是包含 start 索引，不包含 end 索引的,索引0代表着第一个元素
name=['lawa','wang','luo','shuang']
print(name[0:3])#所以只会输出前三位
print(name[:3])   # 没有第一个索引，python将自动从列表开头开始，等价于 name[0:3]，不包含最后一个元素
print(name[:])    # 等价于 name[0:len(name)]，包含所有元素
print(name[2:])   #将返回从第3个元素到列表末尾的所有元素
print(name[-3:])    #负数索引表示从列表末尾开始计数（-1 是最后一个元素，-2 是倒数第二个，依此类推），相当于输出倒数第三个元素到末尾

name = ['lawa', 'wang', 'luo', 'shuang']
new_list = [item.title() for item in name[0:3]]#这样能够输出前三位
print(new_list)

#遍历切片
name=['lawa','wang','luo','shuang']
for player in name[:3]:
    print(player.title())
#复制列表:需要省略起始索引和终止索引
name1=name[:]#相当于对上述的列表进行复制
print(name1)#name1和name相当于是两个列表
name.append('ALex')
name2=name#实际上name2和name指向的是同一个列表
print(name2)


#遍历元组
dimensions=(200,50)
for dimension in dimensions:
    print(dimension)

#修改元组的变量：元组定义好后，元组里的变量不可以修改，但是可以给存储元组的变量赋
dimensions=(200,50)
print("最初的元组：")
for dimension in dimensions:
    print(dimension)
dimensions=(400,1000)#将一个新的元组赋值给变量dimensions，这并不会修改原始的元组，而实创建了一个新的元组
print("\n修改后的为")
for dimension in dimensions:
    print(dimension)