# coding:utf-8

# 函数是带名字的代码块
# 当程序中需要多次执行同一项任务的时候，无需反复编写该任务的代码，只需调用执行该任务的函数

# 定义函数def
def greet_uesr():
    """"显示简单的问候语"""  # 文档字符串，用来描述该函数是做什么的
    print("Hello!")


greet_uesr()  # 调用函数，直接输入函数名()

# 向函数传递信息


def greet_uesr(user_name):
    """"显示简单的问候语"""  # 文档字符串，用来描述该函数是做什么的
    print("Hello!"+user_name.title())


greet_uesr('lawa')  # 调用函数，直接输入函数名()

# 实参和形参
# 形参是函数定义时括号中的变量：user_name
# 实参是调用函数时，传递给函数的信息，比如'lawa'


def favorite_movie(title):
    """显示最喜欢看的电影"""
    print("My favorite movie is:"+title.title()+".")


favorite_movie("pride and prejudice")

# 传递实参
# 向函数传递实参，可以使用位置实参，此时实参的顺序与形参的顺序要相同；
# 也可采用关键字实参，每个实参由变量名和值组成；或者使用字典和列表

# 位置实参：最简单的关联方式基于实参的顺序!!!一定要注意参数的顺序


def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\n I have a "+animal_type+'')
    print("My "+animal_type+"'s name is "+pet_name.title()+".")


describe_pet('hamster', 'hurry')

# 可以根据需要调用函数多次
describe_pet('dog', 'rubby')

# 关键字实参：不需要考虑顺序，类似于试卷上写有每个人的名字，最后是否按照顺序收都不会弄错
# 但是必须了解形参的每个含义


def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\n I have a "+animal_type+'.')
    print("My "+animal_type+"'s name is "+pet_name.title()+".")


describe_pet(animal_type='hamster', pet_name='hurry')
describe_pet(pet_name='rubby', animal_type='dog')
# 使用关键字实参这种方法时，调用各个函数时，需要明确指出各个实参对应的形参，可以不用关心具体的顺序

# 默认值：可以给每个形参指定默认值,给形参指定默认值，可以在函数调用中省略相应的实参


def describe_pet(pet_name, animal_type='dog'):  # 形参列表必须先列出没有默认值的形参，再列出有默认值的形参
    """显示宠物的信息"""
    print("\n I have a "+animal_type+'.')
    print("My "+animal_type+"'s name is "+pet_name.title()+".")


describe_pet(pet_name='hurry')
describe_pet(pet_name='rubby')
describe_pet('Willie')  # 不需要指定，可以直接调用
describe_pet(animal_type='hamster', pet_name='Lucy')  # 就算指定了默认值，也可以自行更改

# 等效函数的调用


# def describe_pet(pet_name, animal_type='dog'):
# 基于此种定义在任何情况下都必须要给pet_name提供实参
describe_pet('willim')
describe_pet(pet_name='willim')
describe_pet('harry', 'hamster')
describe_pet(pet_name="harry", animal_type="hamster")
describe_pet(animal_type='hamster', pet_name='hurry')

# 当提供的实参多于或少于函数完成其工作所需的信息时，会出现实参不匹配的错误
# 根据函数的定义，指定相应的实参

# 当函数不是直接显示输出时，可以设置一个返回值，利用return将值返回到调用函数的代码行，便于简化主程序
# 在分别需要存储大量参数的大型程序当中，利用return非常有用


def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name+' '+last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')  # 调用返回值的函数时，需要提供一个变量，用于存储返回的值
print(musician)

# 让实参变成可以选择的
def get_formatted_name(first_name, middle_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name+' '+middle_name+' '+last_name
    return full_name.title()  # title是让所有的首字母都大写


# 调用返回值的函数时，需要提供一个变量，用于存储返回的值
musician = get_formatted_name('jimi', 'lee', 'hendrix')
print(musician)
# 为了让中间名变成可选的，可以给middle_name指定一个空字符串的默认值，用户未提供时，可以不适用这个实参
def get_formatted_name(first_name, last_name, middle_name=" "):  # 此时要将middle_name移到形参的末尾
    """返回整洁的姓名"""
    if middle_name:#python会将非空的字符串解读为True
        full_name = first_name+' '+middle_name+' '+last_name
    else:
        full_name = first_name+' '+last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')  # 调用返回值的函数时，需要提供一个变量，用于存储返回的值
print(musician)
musician = get_formatted_name('jimi', 'hendrix', 'lee')
print(musician)
# 返回字典
def bulid_name(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person
musician = bulid_name('jimi', 'hendrix')
print(musician)

def bulid_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = bulid_name('jimi', 'hendrix')
print(musician)
musician = bulid_person('jimi', 'hendrix', age=27)
print(musician)

# 结合使用的函数和while循环


def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name+' '+last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("enter 'q' at any time to quit")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last_name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, "+formatted_name+"!")


#传递列表,将列表传递给函数后，函数能直接访问其内容，从而提高列表处理的效率
#将一个名字列表传递给一个名为greet_users()的函数，该函数可以问候列表中的每个人
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg="Hello,"+name.title()+'!'
        print(msg)
usernames=['lawa','vivi','wang']
greet_users(usernames)

#在函数中修改列表，在函数中对列表所做的任何修改都是永久性的，能够高效地处理大量数据
    #将要打印的设计存储在一个列表中，打印后再移到另一个列表当中
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]
while unprinted_designs:
    current_design=unprinted_designs.pop()
    print("Printing model:"+current_design)
    completed_models.append(current_design)
print("\nThe following models have been printed:")
for compelted_model in completed_models:
    print(compelted_model)

#将上述代码编写为两个函数，使效率更高
completed_models=[]
def print_models(unprinted_designs,completed_models):
    """模拟每个打印设计,直到没有未打印的设计为止,打印每个设计后,都将其移动到列表completed_models中"""
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print("Printing model "+current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """显示打印好的所有的模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs=['ipone case','huawei','vivo']
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
#函数设计的理念：每个函数都应只负责一项具体的工作，第一个函数打印每个设计，第二个显示已经打印好的模型，优于使用一个函数来完成两项工作

#禁止函数修改列表
#向函数传递列表的副本而不是原件，此时函数所作的任何修改都只影响副本，丝毫不会影响原件
#function_name(list_name[:]),利用切片表示法[:]创建列表的副本
print_models(unprinted_designs[:],completed_models)
#此时该函数print_models依然能够完成其工作，但其使用的是列表unprinted_designs的副本，而不是列表unprinted_design本身
#但是将原始的列表传递给函数，能够让函数使用现成的列表，避免花实践和内存创建副本，从而提升效率，大型列表更应该直接使用原列表

#传递任意数量的实参，从调用语句中收集任意数量的实参
#创建一个制作披萨的函数，由于不知道要多少种配料，所以先使用后形参*toppings
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)
    #形参名*toppings中的*让python创建了一个名为toppings的空元组，并将收到的所有值都封装到该元组当中
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
#将print语句替换为一个循环，对配料表进行遍历，并对顾客点的披萨进行描述
def make_pizza(*toppings):
    print("\nWhat a pizza with the following toppings:")
    for topping in toppings:
        print("-"+topping)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

#结合使用位置实参和任意数量的实参
#为了让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后
#python先匹配位置实参和关键字实参，再将剩余的实参都收集到最后一个形参当中
def make_pizza(size,*toppings):
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("-"+topping)
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

#使用任意数量的关键字实参
#将函数编写成能够接受任意数量的键-值对
    #示例：利用函数接受名和姓，同时还接受任意数量的关键字实参：
def build_profile(first,last,**user_info):
    #python中函数参数变量名一个*表示元组，两个**表示动态字典
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile
user_profile=build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)

#将函数存储在模块当中
#将函数存储为被称为模块的独立文件中，再将模块导入到主程序之中，import语句允许在当前运行的程序文件中使用模块中的代码
#即将代码模块化，有利于代码的复用
