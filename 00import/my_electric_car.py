#在同一个模块中存储多个类，多个的类需要存在某种相关性
from car import ElectricCar,Car
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_beetle=Car('volkswagen','bettle',2016)
print(my_beetle.get_descriptive_name())

#导入整个car模块
import car
my_beetle=car.Car('volkswagen','bettle',2016)
print(my_beetle.get_descriptive_name())
my_tesla=car.ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

