# 自定义异常类，继承Exception
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    # 设置抛出异常的描述信息
    def __str__(self):
        return f'你输入的长度为{self.length}，不能少于{self.min_len}个字符'


def main():
    try:
        con = input('请输入密码：')
        if len(con) < 3:  # 即输入密码不符合要求
            raise ShortInputError(len(con), 3)  # 抛出异常 raise
    except Exception as result:
        print(result)
    else:
        print('密码输入完成')

main()