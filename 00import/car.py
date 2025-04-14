class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):  # 初始化汽车的品牌、型号、年份和里程数
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):  # 返回汽车的描述信息
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):  # 打印汽车的当前里程数
        print("This car has "+str(self.odometer_reading)+"miles on it.")

    def update_odometer(self, mileage):  # 更新汽车的里程数
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):  # 增加汽车的里程数
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
