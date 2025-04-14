# 导入函数的整个模块
from pizza import *
import pizza as p
from pizza import make_pizza as mp
from pizza import make_pizza
import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 导入特定的函数
# from module_name import function_name
# 利用逗号分割函数名，可根据需要从模块中导入任意数量的函数

#   from module_name
#   import function_0,function_1,function_2

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用as给函数指定别名   语法：from module_name import function_name as fn
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用as给模块指定别名，只更改了模块名，函数名并未发生改变，使代码更加简洁，更专注于描述性函数名
# 语法 import module_name as mn
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 导入模块中的所有函数，使用*
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# python可能遇到多个名称相同的函数或变量，进而覆盖函数，故最好不采用这样的方法，最好分别导入你需要使用的函数
#
