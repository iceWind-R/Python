'''
1、导包 socket
2、初始化一个socket
3、调用socket的一个方法发送数据
4、关闭socket
'''


import socket


# AF_INET  ip地址的类型：ipv4
# SOCK_DGRAM  UDP协议
send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


send_socket.sendto('UDPUDPUDPU董奥'.encode('utf-8'), ('192.168.56.1',8080))

send_socket.close()