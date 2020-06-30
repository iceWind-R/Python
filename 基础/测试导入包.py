# import myPackage.my_module1
#
# myPackage.my_module1.info_print1()

# 第二种导入包
# 设置__init__.py文件里面的all列表，添加的是允许导入的模块

from myPackage import *
my_module1.info_print1()