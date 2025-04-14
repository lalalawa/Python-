# 导入单个Car类
#from 模块名 import 类名，从某个模块导入某个类
from car import Car
my_new_car = Car('audi', 'A4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

