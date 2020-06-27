def info_print():
    print('请选择功能')
    print('1、添加学生')
    print('2、删除学生')
    print('3、修改学生')
    print('4、查询学生')
    print('5、显示所有学员')
    print('6、退出系统')
    print('*' * 20)

info =[] #存储的所有学生信息，其中的每个数据都为一个字典型

def add_info():
    # 用户输入数据
    new_id = input('请输入学号：')
    new_name = input('请输入姓名：')
    new_phone = input('请输入电话：')

    #判断信息是否已经存在
    global info
    for i in info:
        if new_name == i['name']:
            print('此用户已经存在')
            return

    info_dict = {} # 学生信息字典

    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['phone'] = new_phone

    #列表追加字典
    info.append(info_dict)
    print(info)

def del_info():
    del_name = input('请输入删除的学生姓名：')

    global info
    for i in info:
        if(del_name == i['name']):
            info.remove(i)
            break
    else:
        print('该学生不存在')

    print(info)

def modify_info():
    modify_name = input('请输入修改的学生姓名：')

    global info
    for i in info:
        if modify_name == i['name']:
            i['phone'] =  input('请输入修改后的手机号：')
            break
    else:
        print('该学生不存在')
    print(info)

def search_info():
    search_name = input('请输入查询学生姓名：')
    global info
    for i in info:
        if search_name == i['name']:
            print('查询到的学生信息如下：')
            print(f"学生的学号为：{i['id']}，姓名为：{i['name']}，电话为：{i['phone']}")
            break
    else:
        print('查询此人失败')

def print_all():
    print('学号\t姓名\t手机号')
    for i in info:
        print(f"{i['id']}\t\t{i['name']}\t\t{i['phone']}")

while True:
    info_print()
    user_num = int(input('请输入功能序号：'))

    if user_num == 1:
        add_info()
    elif user_num == 2:
        del_info()
    elif user_num == 3:
        modify_info()
    elif user_num == 4:
        search_info()
    elif user_num == 5:
        print_all()
    elif user_num == 6:
        if input('确认退出吗?(Yes or No)') == 'Yes':
            break
    else:
        print('输入有误，请重新输入！')

print('退出系统成功！欢迎下次使用')

