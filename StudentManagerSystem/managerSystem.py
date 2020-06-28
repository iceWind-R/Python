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
                print('退出成功，欢迎下次使用。')
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

        self.show_student()

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
            print('删除失败，查无此人')

        self.show_student()

    # 修改学生
    def modify_student(self):
        modify_name = input('请输入要修改的学生姓名：')

        for i in self.student_list:
            if modify_name == i.name:
                i.name = input('姓名')
                i.gender = input('性别')
                i.tei = input('电话')
                print(f'修改学生信息成功，姓名：{i.name}，性别：{i.gender}，电话：{i.tel}')
                break
        else:
            print('修改失败，查无此人')

        self.show_student()

    # 查询学生
    def search_student(self):
        search_name = input('请输入查询的学生姓名：')

        for i in self.student_list:
            if search_name == i.name:
                print(f'学生信息查询成功，姓名：{i.name}，性别：{i.gender}，电话：{i.tel}')
                break
        else:
            print('查询失败，查无此人')

    # 显示学生
    def show_student(self):
        print('-' * 5 + '所有学生信息' + '-' * 5)
        print('姓名\t性别\t电话')
        for i in self.student_list:
            print(i.name, end='\t\t')
            print(i.gender, end='\t\t')
            print(i.tel)
        print('-' * 21)

    # 保存学生
    def save_student(self):
        # 打开文件
        f = open('student.data', 'w')

        # 文件写入数据
        # [学生对象] 转换成 [字典]
        new_list = [i.__dict__ for i in self.student_list]
        print(str(new_list))

        # 文件写入 字符串数据
        f.write(str(new_list))

        # 关闭文件
        f.close()

    # 加载学生
    def load_student(self):
        # 1、打开文件：尝试r打开，有异常w打开
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            # 读取数据：文件读出的数据是字符串，还原为列表类型：[{}] 转换 [学生对象]
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
        finally:
            f.close()
