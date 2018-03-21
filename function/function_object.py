from functools import reduce
from inspect import signature
import operator
from functools import partial

# 函数也是对象，它有自己的属性，可以赋值，做函数参数或返回值
def factorial(n):
    # 函数首行的注释用于生成文档，执行help(factorial)会展示该内容
    '''return n!'''
    return 1 if n < 2 else n * factorial(n -2)

print(factorial.__name__)
print(factorial.__doc__)
print(type(factorial))
print(factorial(10))

# 常用内置高阶函数

# 使用map计算阶层列表
l = map(lambda x: x*x, range(1, 11))
print(list(l))


# 使用列表推导计算阶层列表
print([x*x for x in range(1, 11)])

# 使用reduce求阶层
def f(x, y): return x*y
print(reduce(f, range(1, 11)))

# 使用filter过滤奇数
print(list(filter(lambda x: x%2==0, range(1, 11))))

# 使用列表推导过滤奇数
print([x for x in range(1, 11) if x%2==0])

# all():当列表中的值都为真是返回True，否则返回False
# any():当列表中的值至少有一个为真时返回True，否则返回False
print(all([True, [1]]))
print(any([True, [1]]))
print(all([True, []]))
print(any([True, []]))


# 重载了__call__()方法的类为可调用对象
class Fun(object):
    def __call__(self, *args, **kwargs):
        print('Fun')

fun = Fun()
fun()

# callable()用于判断是否是可调用对象
print(callable(lambda x: x))
print(callable(Fun))

# 列出函数的所有属性
print(dir(factorial))
# 用户自定义的属性
print(factorial.__dict__)


def fun(a, b, c=10, *d, **e):
    x = a + b + c
    return x

# 函数参数个数，不包括* 和 **
print(fun.__code__.co_argcount)
# 前N个为函数参数，后面为函数内部定义的局部变量
print(fun.__code__.co_varnames)
# 函数参数默认值
print(fun.__defaults__)

# 通过inspect包可以方便的获取参数默认值
sig = signature(fun)
print(sig)

for name, param in sig.parameters.items():
    print(param.kind, ": ", name, " = ", param.default)


# 可以给函数参数和函数返回值添加注解
# 注解可以是类型或字符串，含有默认值的参数，注解存在参数可以=之间
def max(a:int, b:int, p:'print'=False) -> int:
    m = a if a>b else b
    if p:
        print(m)
    return m

# 注解保存在__annotations__属性中，除此之外不会做任何处理
print(max.__annotations__)
print(max(1, 2))


# operator包提供了很多运算符的函数形式
print(operator.mul(1, 2))

# itemgetter(N)是一个可以用于返回序列中第N个元素的函数对象
print(operator.itemgetter(2)(range(10)))
# itemgetter的参数可以有多个，此时会返回一个元组
print(operator.itemgetter(2, 5)(range(10)))

d = {'a':1, 'b':2}
# itemgetter使用[]，因此也支持字典和任何实现__getitem__的类型
print(operator.itemgetter('a')(d))

# 类型与C++中的bind
mul10 = partial(operator.mul, 10)
print(mul10(10))