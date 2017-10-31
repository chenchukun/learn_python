# 可以使用相对导入来导入其他子模块，因为主模块的名字总是 "__main__" ，Python 应用程序的主模块应该总是用绝对导入。
from ..sub_package1 import sub_all