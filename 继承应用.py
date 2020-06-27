# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu =  '经典配方'

    def make_cake(self):
        print(f'运用的技术：{self.kongfu}')

# 学校类
class School(object):
    def __init__(self):
        self.kongfu = '新式配方'

    def make_cake(self):
        print(f'运用的技术：{self.kongfu}')

# 徒弟类
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '独创配方'

    def make_cake(self):
        # 加入自己的init方法原因：如果先调用了父类的属性和方法，父类属性回覆盖子类属性
        self.__init__()
        print(f'运用的技术：{self.kongfu}')

    # 子类调用父类的同名方法和属性：即把父类的同名方法和属性再次封装
    def make_master_cake(self):
        # 父类名.函数
        Master.__init__(self) # 调用初始化的原因：这里想要调用父类的同名方法和属性，属性在父类的init方法中被初始化，所以此处再次调用
        Master.make_cake(self)

    def make_school_cake(self):
        # 父类名.函数
        School.__init__(self)
        School.make_cake(self)

daqiu = Prentice()
daqiu.make_master_cake()
daqiu.make_school_cake()