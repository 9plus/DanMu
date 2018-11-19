# coding=utf-8

import multiprocessing
import socket
import time
import re
import signal


# 弹幕查询正则表达式
class DataRegex:
    def __init__(self):
        self.danmu_regex = re.compile(b'txt@=(.+?)/cid@')
        self.username_regex = re.compile(b'nn@=(.+?)/txt@')
        self.level_regex = re.compile(b'level@=(.+?)/nl@')
        self.card_regex = re.compile(b'bnn@=(.+?)/bl@')
        self.card_level_regex = re.compile(b'bl@=(.+?)/brid@')


class DanMu:
    def __init__(self):
        self.data_regex=DataRegex()
        self.client=self.connect()
    

    def connect(self):
        # 构造socket连接，和斗鱼api服务器相连接
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostbyname("openbarrage.douyutv.com")
        port = 8601
        client.connect((host, port))
        return client

    def send_req_msg(self, msgstr):
        #构造并发送符合斗鱼api的请求
        
        msg = msgstr.encode('utf-8')
        data_length = len(msg) + 8
        code = 689
        # 构造协议头
        msg_head = int.to_bytes(data_length, 4, 'little') \
            + int.to_bytes(data_length, 4, 'little') + \
            int.to_bytes(code, 4, 'little')
        self.client.send(msg_head)
        sent = 0
        while sent < len(msg):
            tn = client.send(msg[sent:])
            sent = sent + tn


    def DM_start(self,roomid):
        # 登陆请求
        msg = 'type@=loginreq/roomid@={}/\0'.format(roomid)
        self.send_req_msg(msg)

        msg_more = 'type@=joingroup/rid@={}/gid@=-9999/\0'.format(roomid)
        self.send_req_msg(msg_more)
        # 查找用户名和弹幕内容


        while True:
            data = self.client.recv(4096)
            danmu_username = self.data_regex.username_regex.findall(data)
            danmu_content = self.data_regex.danmu_regex.findall(data)
            danmu_level = self.data_regex.level_regex.findall(data)
            danmu_card_level = self.data_regex.card_level_regex.findall(data)
            danmu_card = self.data_regex.card_regex.findall(data)

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


    def keeplive(self):
        while True:
            msg = 'type@=mrkl/\0'
            self.send_req_msg(msg)
            print('发送心跳包')
            time.sleep(15)

            
    def logout(self):
    
        msg = 'type@=logout/'
        self.send_req_msg(msg)
        print('已经退出服务器')
    def signal_handler(self,signal,frame):
    
        p1.terminate()
        #p2.terminate()
        p3.terminate()
        self.logout()
        print('Bye')


if __name__ == '__main__':
    dan_mu=DanMu()
    room_id1 = 60937
    #room_id2 = 2009
    signal.signal(signal.SIGINT, dan_mu.signal_handler)

    p1 = multiprocessing.Process(target=dan_mu.DM_start, args=(room_id1,))
    #p2 = multiprocessing.Process(target=DM_start, args=(room_id2,))
    p3 = multiprocessing.Process(target=dan_mu.keeplive)
    p1.start()
    #p2.start()
    p3.start()
