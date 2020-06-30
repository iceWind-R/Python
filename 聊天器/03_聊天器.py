import socket


# 定义函数，发送消息
def send_msg(udp_socket):
    msg = input('请输入发送的信息：')
    ip = input('请输入ip地址：')
    port = int(input('请输入端口号：'))
    udp_socket.sendto(msg.encode('utf-8'), (ip, port))


def recv_msg(udp_socket):
    smg = udp_socket.recvfrom(1024)
    print('%s:%s' % (smg[1],smg[0].decode('gbk')))



def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.bind(('192.168.56.1', 8080))

    print('-' * 20)
    print('1、发送消息')
    print('2、接收消息')
    print('-' * 20)
    while True:
        menu_code = input('请输入选项：')

        if menu_code == '1':
            send_msg(udp_socket)
        elif menu_code == '2':
            recv_msg(udp_socket)
        else:
            print('录入有误，请重新输入。')


if __name__ == '__main__':
    main()