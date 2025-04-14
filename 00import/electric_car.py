# 为了避免模块太大，或者在同一个模块中存储不相关的类，需要将类分散到多个模块当中
"""一组可以用于表示电动汽车的类"""
from car import Car


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
