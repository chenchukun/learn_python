#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# 指定当前程序文本编码类型，必须放在前两行

from collections import deque
from math import pi
import importlib
import sys

def testBase():
    print('-------------testBase-------------')
    # 通过切片替换掉指定元素
    l = [1, 2, 3, 4, 5]
    l[1:3] = [9, 8, 7, 6, 5]
    print(l)

    def fib(n):
        a, b = 0, 1
        i = 0
        while i < n:
            # python支持多赋值，且在赋值之前，赋值号右边的表达式会先计算结果，再进行赋值
            a, b = b, a+b
            yield a
            i += 1

    # 使用 ** 时注意优先级
    n = -3 ** 2
    m = (-3) ** 2
    print(n, m)

    for x in fib(10):
        # print的关键字参数可以指定输出结束符
        print(x, end=', ')
    print('')


def testControl():
    print('-------------testControl-------------')
    words = ['cat', 'window', 'defenestrate']
    print(words)
    # 若要在遍历列表的过程中添加或删除元素，可以使用切片对原序列进行拷贝
    for word in words[:]:
        if len(word) > 6:
            words.insert(0, word)
    print(words)

    # range可以有一个与切片类似的step，且可以为负数
    for x in range(-10, -100, -20):
        print(x, end=',')
    print('')

    # for循环可以与else一起使用，表示在循环中为执行break时执行else语句内容。
    # 例：输出10以内的素数
    for n in range(2, 10):
        for m in range(2, n):
            if n % m == 0:
                print('%d is not a prime number' % n)
                break
        else:
            print('%d is a prime number' % n)

    # 函数默认值在定义的时候初始化，且只初始化一次，函数默认值一般使用不变量，否则会出现一些奇怪的现象
    i = 10
    def f(arg=i):
        print(arg)
    i = 11
    f()

    # 函数注解 可以添加函数参数或返回值的类型信息，它对函数本身没有任何影响，可以作为调试信息使用
    def fun(msg:str, num:int) -> str:
        return msg * num

    print(fun('哈', 5))
    # __annotations__属性存储着函数注解信息
    print(fun.__annotations__)

    # 文档字符串，用于描述函数或类的功能，可以使用工具自动生成文档。若有多行，第二行因为空行，
    def fun_doc():
        """No nothing, but document it.

No, really, it doesn't do anything.
        """
        return None

    print(fun_doc.__doc__)
    print('')


def testDataStruct():
    print('-------------testDataStruct-------------')
    l = [1, 2, 3, 4]
    l.append(5)
    l.insert(0, 0)
    # 追加一个列表或元组的所有值到原有列表
    l.extend([6, 7, 8])
    l.extend((9, 10))
    print(l)
    # 删除列表中出现的第一个指定的值
    l.remove(7)
    # 删除并返回指定元素，为指定则删除最后一个元素
    l.pop()
    l.pop(1)
    print(l)
    l2 = l[:]
    # 清空列表
    l2.clear()
    print(l2)
    print(l.index(5))
    print(l.count(5))
    l.sort(key=None, reverse=True)
    print(l)
    # 返回l的浅副本，相当于l[:]
    l2 = l.copy()

    # 双端队列
    q = deque(range(10))
    print(q)
    q.append(10)
    q.appendleft(-1)
    print(q)
    # deque的pop只能删除第一和最后一个元素，不能像列表删除任意下边的元素
    q.pop()
    q.popleft()
    print(q)

    # 列表推导式的每个for都可以有一个if子句
    l = [(x, y) for x in range(10) if x%2==0 for y in range(10) if y%2==1]
    print(l)
    # round取小数点后几位小数
    l = [str(round(pi, i)) for i in range(1, 6)]
    print(l)

    matrix = [ [1, 2, 3, 4], [5, 6, 7, 8],[9, 10, 11, 12] ]
    # 通过列表推导式将转置行和列
    # 列表推导式的第一个表达式可以是任意表达式，甚至是另一个列表推导式
    matrix2 = [[row[i] for row in matrix] for i in range(4)]
    print(matrix2)
    # zip接收任意多个列表，将列表中同一列的元素组装为一个tuple，并返回由这些tuple组成的列表
    print(list(zip(*matrix)))
    # del可以用来删除列表中指定元素，或切片，或删除一个变量
    a = [1, 2, 3, 4, 5]
    del a[0]
    del a[:3]
    print(a)
    del a
    # del变量后不能再使用该变量
    try:
        print(a)
    except UnboundLocalError as e:
        print(e)

    # 元组本身不可变，但若元组元素是可变类型，可改变元素本身的值
    t = (1, 2, 3, [1, 2, 3])
    print(t)
    t[3].append(4)
    print(t)
    # 初始化元组可以不使用()
    t = 1, 2, 3
    print(t)
    # 元组拆包
    a, b, c = t
    print(a, b, c)

    # 可以使用{}来创建一个集合，创建空集合时需要使用set()而不能使用{}
    s = {'a', 'b', 'c', 'c'}
    print(s)
    # set构造函数接收的是一个iterator
    s = set('hello')
    print(s)
    s = set(('hello', 'world'))
    print(s)
    a = set('hello')
    b = set('world')
    print(a - b)
    print(a | b)
    # set不支持 + 运算，应使用&运算
    print(a & b)
    print(a ^ b)
    # 类似于列表推导，集合也支持推导式
    s = {x for x in 'hello' if x<'i'}
    print(s)
    s = set([(1, 2), (3, 4)])
    print(s)
    # set不支持存储可变类型，因为hash不能操作内置的可变类型
    #s = set([[1, 2], [3, 4]])

    # dict的构造函数可以接受一个元组列表
    d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    print(d)
    # 当key时字符串时，可以使用类似于关键字参数的方式来初始化dict
    d = dict(name='cck', age=25)
    print(d)
    # dict不知道可变类型作为key，即使是tuple中包含可变类型也不行
    #d = {(1, 2, [1, 2]):'[1,2]'}
    # dict也支持推导式
    d = {x:y for x in range(0,5) for y in range(5, 10)}
    print(d)
    # keys返回的是dict的y一个字典视图对象，它不是独立于原有字典的，而是基于原有字典的
    ks = d.keys()
    print(ks)
    # 修改字典后，原来通过keys()获取的字典视图对象也跟着变化了
    d[5] = 10
    print(ks)

    # 使用zip可以用来tton同时遍历多个序列
    l = [1, 2, 3]
    l2 = [4, 5, 6]
    for x, y in zip(l, l2):
        print(x, y)
    # 使用reversed反向迭代一个序列
    for x in reversed(l):
        print(x, end=',')
    print('')
    # 若在遍历序列的过程中想修改序列，则创建新的序列会更加的安全
    # 可以利用逻辑运算符的短路特点来进行一些特殊的操作
    string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
    non_null = string1 or string2 or string3
    print(non_null)
    # python中，混合比较不同类型的变量是合法的，只要该类型支持比较运算
    print(set('hello') == list('hello'))
    print('')


from package2.sub_package1 import *
def testModule():
    print('-------------testModule-------------')
    # 导入模块时执行三个步骤：1、搜索。2、编译。3、运行
    # 模块中包含的可执行语句用于初始化模块，它只有在整个进程中第一次导入时执行一次
    import module1
    # 可以通过__name__来获取模块名
    print(module1.__name__)
    import module2
    print(module2.__name__)
    # from * import * 只能在全局使用，不能在函数内部使用，
    # 它将模块中所有名称复制到当前模块的符号表，但不会导入以_开头的名称，通过显式的指定可以导入
    # from * import * 不会执行模块中的可执行语句，import指定名称会
    #from module1 import *
    #print(public)
    #print(_private)
    # 若要改变模块中全局变量的值并让其他模块说知道，需要通过模块名来指定，
    # 若是通过将模块中的全局变量导入到模块的符号表后进行修改，其他模块无法知道该值的变化。
    print((module1.public))
    import module3
    print(module1.public)
    # 若模块中的变量是可变类型，则通过from * import *导入时复制的是引用，通过引用修改该对象其他模块可以发现
    # 切记：from * impot * 是将模块中所有顶层名称赋值给当前模块相同的名称。
    print(module1.l)
    import module4
    print(module1.l)
    # 通过importlib模块的reload函数可以重新加载模块，重新加载模块会执行初始化语句
    importlib.reload(module3)
    # python模块中可运行的表达式到底是什么时候执行的？如何执行的？
    from module4 import out
    print('module4')
    out()

    # 导入模块时，解释器会在内置模块的搜索路径中查找该模块，若未找到则在sys.path给出的路径中查找
    # sys.path默认包含运行的python文件所在路径
    print(sys.path)
    sys.path.insert(0, '/')
    print(sys.path)
    # 为了加快加载模块的速度，Python在__pycache__目录下缓存每个模块编译好的版本，名称为module.version.pyc，
    # 从.pyc文件读取的程序不会比从.py文件读取的程序的运行速度更快，.pyc文件唯一快的地方在于它们加载的速度。
    # 只要被导入的模块才会被编译，顶层模块一般不会被编译，它被设计为直接直接执行

    # dir()函数用来找出模块中定义了哪些名字，包括变量、模块、函数等
    print(dir(module1))
    print(dir())
    # dir()不会列出内置的函数和变量的名称。可以使用dir(builtins)列出
    import builtins
    print(dir(builtins))

    # 可以使用from package import item来导入子模块或包，item可以是子模块，子包或模块中的名称
    from package1.sub_package1 import sub
    sub.sub()
    # 也可以使用import来导入，这种情况下，处理最后一项，其他项必须是一个包，最后一项可以说模块或包，但不能是模块中的名称
    import package1.sub_package1.sub
    package1.sub_package1.sub.sub()
    # from package2.sub_package1 import * 通过*想导入一个包下的模块时，Python默认不会导入包下的所有模块
    # 想要在这种情况下导入模块，需要在__init__中定义__all__变量
    # 使用import *不是一个好习惯，应避免使用
    sub_all.all()
    print('')


def testIO():
    print('-------------testIO-------------')
    # 在字符串两侧填充空格，实现左对齐，右对齐和居中
    print('name'.rjust(10), 'sex'.rjust(10), 'age'.rjust(10))
    print('cck'.rjust(10), 'male'.rjust(10), '25'.rjust(10))
    print('name'.ljust(10), 'sex'.ljust(10), 'age'.ljust(10))
    print('cck'.ljust(10), 'male'.ljust(10), '25'.ljust(10))
    print('name'.center(10), 'sex'.center(10), 'age'.center(10))
    print('cck'.center(10), 'male'.center(10), '25'.center(10))
    # 在字符串左侧填充0
    print('12'.zfill(5))

    # str.format()用来格式化字符串
    print('name: {}, age:{}'.format('cck', 25))
    print('name: {1}, age:{0}'.format(25, 'cck'))
    print('name: {name}, age:{age}'.format(name='cck', age=25))
    d = dict(name='cck', age=25)
    print('name: {name}, age:{age}'.format(**d))
    contents = 'eels'
    # !a 运用ascii()  !s 运用str()  !r 运用repr()
    print('My hovercraft is full of {!r}'.format(contents))
    # .xf 指定浮点数小数位数
    print('PI: {:.2f}'.format(pi))
    # :x 指定位数
    print(d)
    for name, age in d.items():
        print('{0:10} ==> {1:10}'.format(name, str(age)))

    with open('module1.py', 'r') as f:
        # f.tell() 返回文件指针的当前位置，在二进制模式中表示字节数，文本模式中则不准确
        print(f.tell())
        # f.seek(offset, from_what), from_what的值为0, 1, 2，分别边上文件开头、当前文件位置、和文件结尾
        f.seek(1, 0)
        print(f.tell())
        print(f.closed)
        print('')


def testException():
    print('-------------testException-------------')
    try:
        f = open('data.txt', 'r')
    except (FileNotFoundError, FileExistsError) as e:
        print(e.strerror)
        print(e.args)
    except:
        print('Other exception')
    else:
        print('Not exception')
    finally:
        print('Goodbye')
    try:
        raise Exception('Error')
    except Exception as e:
        print(e.args)
    print('')


def testClass():
    print('-------------testClass-------------')
    # 作用域
    def doLocal():
        # spam为局部变量
        spam = 'local spam'
    def doNonlocal():
        # 声明nonlocal并不需要外层变量在之前已赋值过
        nonlocal spam
        # spam为外层变量
        spam = 'nonlocal spam'
    def doGlobal():
        # 声明global并不需要外层变量在之前已赋值过
        global spam
        # spam为模块级变量
        spam = 'global spam'
    spam = 'test'
    print(spam)
    doLocal()
    print(spam)
    doNonlocal()
    print(spam)
    doGlobal()
    print(spam)

    class Test:
        i = 10
        def f(self):
            i = 1
    test1 = Test()
    test2 = Test()
    print(Test.i)
    print(test1.i)
    print(test2.i)
    # 通过类名对类内最外层变量赋值，会影响所有该类对象的值
    Test.i = 20
    print(Test.i)
    print(test1.i)
    print(test2.i)
    # 通过对象对类内最外层变量赋值，只会影响当前对象的值
    test1.i = 30
    print(Test.i)
    print(test1.i)
    print(test2.i)


if __name__ == '__main__':
    testBase()
    testControl()
    testDataStruct()
    testModule()
    testIO()
    testException()
    testClass()
    print(spam)
