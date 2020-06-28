class A(object):
    a = 0

    def __init__(self):
        self.b = 1

a = A()
# 返回类内部所有属性和方法对应的字典
print(A.__dict__)
# 返回实例属性和值组成的字典
print(a.__dict__)