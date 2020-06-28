from student import *

class StudentManager(object):
    def __init__(self):
        # 存储学生数据的列表
        self.student_list = []

    # 一、程序入口函数
    def run(self):
        # 1、加载文件里的学生信息
        self.load_student()
        while True:
            # 2、显示功能菜单
            self.show_menu()
            # 3、用户输入目标功能序号
            menu_num = int(input('请输入功能序号：'))
            # 4、根据用户的序号执行不同的功能
            if menu_num == 1:
                # 添加学生
                self.add_student()
            elif menu_num == 2:
                # 删除学生
                self.del_student()
            elif menu_num == 3:
                # 修改信息
                self.modify_student()
            elif menu_num == 4:
                # 查询信息
                self.search_student()
            elif menu_num == 5:
                # 显示信息
                self.show_student()
            elif menu_num == 6:
                # 保存信息
                self.save_student()
            elif menu_num == 7:
                # 退出系统 -- 退出循环
                break

    # 二、系统功能函数
    # 1、显示功能菜单 -- 静态方法
    @staticmethod
    def show_menu():
        print('1、添加学生')
        print('2、删除学生')
        print('3、修改信息')
        print('4、查询信息')
        print('5、显示信息')
        print('6、保存信息')
        print('7、退出系统')

    # 添加学生
    def add_student(self):
        # 用户输入信息
        name = input('请输入您的姓名：')
        gender = input('请输入您的性别：')
        tel = input('请输入您的电话：')

        # 创建学生对象 -- 类在student文件里，先导入student模块，再创建对象
        student = Student(name, gender, tel)

        # 将该对象添加到学生列表
        self.student_list.append(student)

        print('姓名\t性别\t电话')
        for i in self.student_list:
            print(i.name,end='\t\t')
            print(i.gender,end='\t\t')
            print(i.tel)

    # 删除学生
    def del_student(self):
        # 用户输入学生姓名
        del_name = input('请输入要删除的学生姓名：')

        # 遍历学生列表
        for i in self.student_list:
            if del_name == i.name:
                self.student_list.remove(i)
                break
        # 循环后，即查无此学生
        else:
            print('查无此人')

        print('删除后：'+self.student_list)

    # 修改学生
    def modify_student(self):
        print('修改学生')

    # 查询学生
    def search_student(self):
        print('查询学生')

    # 显示学生
    def show_student(self):
        print('显示学生')

    # 保存学生
    def save_student(self):
        print('保存学生')

    # 加载学生
    def load_student(self):
        print('加载学生')