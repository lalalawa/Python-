# coding:utf-8

# 创建和使用类
# 创建Dog类
# 在python中类常以大写字母开头进行命名，类定义了一种对象的属性
class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):  # 是一个初始化的函数
        # __init__被称为类的构造函数，创建类的新实例时，该函数会自动被调用
        # self代表类的实例本身，会自动传递该实例作为第一个参数给_init_函数，使用self来访问实例的属性和方法
        # 通过实参向Dog()传递了名字和年龄，self会自动传递，
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        print(self.name.title()+" rolled over!")


# 创建一个 Dog 类的实例
my_dog = Dog("buddy", 3)
# 调用实例的方法
my_dog.sit()
my_dog.roll_over()

# 根据类创建实例
my_dog = Dog('Willie', 6)
print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old")

# 创建多个实例，每条小狗都是一个独立的实例，有自己的一组属性，能够执行相同的操作
# 通过创建类能够提高代码的复用性
my_dog = Dog("Willie", 6)
your_dog = Dog('lucy', 3)
print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
my_dog.sit()
print("\nYour dog's name is "+your_dog.name.title()+".")
print("Your dog is "+str(your_dog.age)+" years old.")
your_dog.sit()


# 使用类和实例
class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()


my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())

# 给属性指定默认值
# 类中的每个属性都必须有初始值，哪怕该值为0或者是空字符串


class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 添加一个名为odometer_reading的属性，初始值始终为0，用于读取汽车的里程表
    # 属性可以添加，但是不在括号内的属性无法被调用，只能通过间接调用

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")


my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
# 修改属性的值，可通过三种方式
# 直接修改属性的值
my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# 通过方法修改属性的值


class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 添加一个名为odometer_reading的属性，初始值始终为0，用于读取汽车的里程表
    # 属性可以添加，但是不在括号内的属性无法被调用，只能通过间接调用

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        self.odometer_reading = mileage


my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(25)
my_new_car.read_odometer()

# 添加一些逻辑，禁止任何人将里程表读数往回调


class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 添加一个名为odometer_reading的属性，初始值始终为0，用于读取汽车的里程表
    # 属性可以添加，但是不在括号内的属性无法被调用，只能通过间接调用

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    # 通过方法对属性的值进行递增


class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 添加一个名为odometer_reading的属性，初始值始终为0，用于读取汽车的里程表
    # 属性可以添加，但是不在括号内的属性无法被调用，只能通过间接调用

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


my_uesed_car = Car('subaru', 'outback', 2013)
print(my_uesed_car.get_descriptive_name())
my_uesed_car.update_odometer(23500)
my_uesed_car.read_odometer()
my_uesed_car.increment_odometer(100)
my_uesed_car.read_odometer()
# 在python中，定义一个类的方法后，若要调用该方法，需要在方法名后面加上()，括号是触发方法的执行，传入方法所需的参数
# """三个双引号括起来的内容是文档字符串，用来对类、方法、函数或者模块进行说明，能够帮助其他开发者理解代码的功能和使用"""

# 若编写的类是另一个现成类的特殊版本，可以使用继承。原有的类叫做父类，新类称为子类，子类继承父类的所有属性和方法，同时还可以定义自己的属性方法
# 子类的方法__init__()，创建子类需要先给父类的所有属性赋值


class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometera(self):
        print("This car has"+str(self.odometer_reading)+"miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
# 创建子类时，父类必须包含在当前的文件之中，且位于子类的前面


class ElectricCar(Car):  # 定义子类时，括号内必须要指定父类的名称
    """"电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类属性"""
        super().__init__(make, model, year)  # super函数帮助python将父类和子类关联起来，就是强行将父类和子类关联起来


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# 给子类定义属性和方法


class ElectricCar(Car):  # 定义子类时，括号内必须要指定父类的名称
    """"
    电动汽车的独特之处
    初始化父类的属性，再初始化电动汽车特有的属性
    """

    def __init__(self, make, model, year):
        """初始化父类属性"""
        super().__init__(make, model, year)  # super函数帮助python将父类和子类关联起来，就是强行将父类和子类关联起来
        self.battery_size = 70

    def describe_battery(self):
        """"打印一条描述电瓶容量的消息"""
        print("This car has a "+str(self.battery_size)+"-kwh battery")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# 重写父类的方法
# 在子类中定义一个与父类名称相同的类，即重写父类，优先级：子类>父类


class ElectricCar(Car):  # 定义子类时，括号内必须要指定父类的名称
    """"
    电动汽车的独特之处
    初始化父类的属性，再初始化电动汽车特有的属性
    """

    def __init__(self, make, model, year):
        """初始化父类属性"""
        super().__init__(make, model, year)  # super函数帮助python将父类和子类关联起来，就是强行将父类和子类关联起来
        self.battery_size = 70

    def describe_battery(self):
        """"打印一条描述电瓶容量的消息"""
        print("This car has a "+str(self.battery_size)+"-kwh battery")

    def fill_gas_tank(self):  # 调用时，可以忽略Car类中的fill_gas_tank
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# 将实例用作属性
# 当给类添加的细节越来越多，需要将类的一部分作为一个独立的类提取出来，将大型的类拆分成多个协同工作的小类。


class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):#初始化汽车的品牌、型号、年份和里程数
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):#返回汽车的描述信息
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):#打印汽车的当前里程数
        print("This car has "+str(self.odometer_reading)+"miles on it.")

    def update_odometer(self, mileage):#更新汽车的里程数
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):#增加汽车的里程数
        self.odometer_reading += miles


class Battery():
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a "+str(self.battery_size)+"-kwh battery")

    def get_range(self):
        """打印一条消息,指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "Tish car can go approximatelt "+str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):  # 定义子类时，括号内必须要指定父类的名称
    """"
    电动汽车的独特之处
    初始化父类的属性，再初始化电动汽车特有的属性
    """

    def __init__(self, make, model, year):
        """初始化父类属性"""
        super().__init__(make, model, year)  # super函数帮助python将父类和子类关联起来，就是强行将父类和子类关联起来
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#Python标准库
#模块collections中的OrderedDict类
"""
顺序性:OrderedDict 会记住元素插入的顺序，在迭代时会按照插入顺序返回元素。
方法兼容性:OrderedDict 支持字典的所有方法，如 items()、keys()、values() 等。
"""
from collections import OrderedDict
favorite_languages=OrderedDict()
favorite_languages['jen']='python'
favorite_languages['sarah']='C'
favorite_languages['edward']='ruby'
favorite_languages['phil']='python'
for name,language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

