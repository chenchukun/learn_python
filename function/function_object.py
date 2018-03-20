from functools import reduce

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