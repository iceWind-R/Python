'''
1、导包 socket
2、初始化一个socket
3、调用socket的一个方法接收数据
4、关闭socket
'''


import socket


# AF_INET  ip地址的类型：ipv4
# SOCK_DGRAM  UDP协议
recv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定ip和端口号
# 参数接收一个元组 ("", 8080) 表示可以接收任何一个电脑发送的数据
recv_socket.bind(('192.168.56.1', 8080))


# 1024 指接受的最大数据（字节）
recvfrom = recv_socket.recvfrom(1024)
print(recvfrom[0].decode('utf-8'))

recv_socket.close()