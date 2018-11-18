# coding=utf-8

import multiprocessing
import socket
import time
import re
import signal

# 构造socket连接，和斗鱼api服务器相连接
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname("openbarrage.douyutv.com")
port = 8601
client.connect((host, port))

# 弹幕查询正则表达式
danmu_regex = re.compile(b'txt@=(.+?)/cid@')
username_regex = re.compile(b'nn@=(.+?)/txt@')
level_regex = re.compile(b'level@=(.+?)/nl@')
card_regex = re.compile(b'bnn@=(.+?)/bl@')
card_level_regex = re.compile(b'bl@=(.+?)/brid@')




def send_req_msg(msgstr):
    '''构造并发送符合斗鱼api的请求'''

    msg = msgstr.encode('utf-8')
    data_length = len(msg) + 8
    code = 689
    # 构造协议头
    msg_head = int.to_bytes(data_length, 4, 'little') \
        + int.to_bytes(data_length, 4, 'little') + \
        int.to_bytes(code, 4, 'little')
    client.send(msg_head)
    sent = 0
    while sent < len(msg):
        tn = client.send(msg[sent:])
        sent = sent + tn



def DM_start(roomid):
    # 登陆请求
    msg = 'type@=loginreq/roomid@={}/\0'.format(roomid)
    send_req_msg(msg)

    msg_more = 'type@=joingroup/rid@={}/gid@=-9999/\0'.format(roomid)
    send_req_msg(msg_more)
    # 查找用户名和弹幕内容


    while True:
        data = client.recv(4096)
        danmu_username = username_regex.findall(data)
        danmu_content = danmu_regex.findall(data)
        danmu_level = level_regex.findall(data)
        danmu_card_level = card_level_regex.findall(data)
        danmu_card = card_regex.findall(data)

        if not data:
            break
        else:
            for i in range(0, len(danmu_content)):
                try:
                    # 输出信息
                    print('[{}级{}  {}]:{}'.format(danmu_card_level[0].decode('utf8'),
                                                       danmu_card[0].decode('utf8'),
                                                       danmu_username[0].decode(
                        'utf8'), danmu_content[0].decode(encoding='utf8')))
                except:
                    continue


def keeplive():
    while True:
        msg = 'type@=mrkl/\0'
        send_req_msg(msg)
        print('发送心跳包')
        time.sleep(15)


def logout():

    msg = 'type@=logout/'
    send_req_msg(msg)
    print('已经退出服务器')


def signal_handler(signal,frame):

    p1.terminate()
    #p2.terminate()
    p3.terminate()
    logout()
    print('Bye')


if __name__ == '__main__':
    #room_id2 = 2009
    room_id1 = 60937
    signal.signal(signal.SIGINT, signal_handler)

    p1 = multiprocessing.Process(target=DM_start, args=(room_id1,))
    #p2 = multiprocessing.Process(target=DM_start, args=(room_id2,))
    p3 = multiprocessing.Process(target=keeplive)
    p1.start()
    #p2.start()
    p3.start()
