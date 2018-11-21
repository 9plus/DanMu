#  coding=utf-8
import re

data1=b'\xf9\x00\x00\x00\xf9\x00\x00\x00\xb2\x02\x00\x00type@=loginres/userid@=0/roomgroup@=0/pg@=0/sessionid@=0/username@=/nickname@=/live_stat@=0/is_illegal@=0/ill_ct@=/ill_ts@=0/now@=0/ps@=0/es@=0/it@=0/its@=0/npv@=0/best_dlev@=0/cur_lev@=0/nrc@=3825205384/ih@=0/sid@=72983/sahf@=0/sceneid@=0/\x00'
data2=b'+\x00\x00\x00+\x00\x00\x00\xb2\x02\x00\x00type@=pingreq/tick@=1542810747604/\x00\x14\x00\x00\x00\x14\x00\x00\x00\xb2\x02\x00\x00type@=mrkl/\x00'
data=b'>\x01\x00\x00>\x01\x00\x00\xb2\x02\x00\x00type@=dgb/rid@=9999/gid@=-9999/gfid@=824/gs@=1/uid@=406114/nn@=M\xe4\xb8\xb6\xe4\xb8\x8d\xe8\xaf\xb7\xe8\x87\xaa\xe6\x9d\xa5/ic@=avanew@Sface@S201711@S27@S13@S86c5ba1ca9e3f2a3c156f1def567abee/eid@=0/level@=17/dw@=0/gfcnt@=1/hits@=8/bcnt@=8/bst@=1/ct@=0/el@=/cm@=0/bnn@=\xe5\xb0\x8f\xe5\x83\xb5\xe5\xb0\xb8/bl@=6/brid@=9999/hc@=8ccfd113d28375263b0964c7221773bf/sahf@=0/fc@=0/gpf@=1/\x00#\x01\x00\x00#\x01\x00\x00\xb2\x02\x00\x00type@=chatmsg/rid@=9999/ct@=2/uid@=16841813/nn@=\xe5\x83\xb5\xe5\xb0\xb8\xe7\x8e\x8brua/txt@=\xe4\xb8\x90\xe5\xb8\xae\xe6\xaf\x8f\xe6\x97\xa5\xe7\xa6\x8f\xe5\x88\xa9/cid@=2006a18e487a490638fb010000000000/ic@=avatar@S016@S84@S18@S13_avatar/level@=20/sahf@=0/cst@=1542810746690/bnn@=\xe5\xb0\x8f\xe5\x83\xb5\xe5\xb0\xb8/bl@=12/brid@=9999/hc@=8ccfd113d28375263b0964c7221773bf/el@=/lk@=/fl@=12/\x00r\x01\x00\x00r\x01\x00\x00\xb2\x02\x00\x00type@=dgb/rid@=9999/gid@=-9999/gfid@=192/gs@=1/uid@=16574659/nn@=\xe5\x94\xaf\xe4\xbd\x99\xe7\x9b\xb8\xe6\x80\x9d/ic@=avanew@Sface@S201802@S25@S12@Sbc16f34d28234985806b069705bb2d7c/eid@=0/level@=18/dw@=0/gfcnt@=1/hits@=2/bcnt@=2/bst@=1/ct@=0/el@=eid@AA=1500000113@ASetp@AA=1@ASsc@AA=1@ASef@AA=0@AS@S/cm@=0/bnn@=\xe5\xb0\x8f\xe5\x83\xb5\xe5\xb0\xb8/bl@=11/brid@=9999/hc@=8ccfd113d28375263b0964c7221773bf/sahf@=0/fc@=0/gpf@=1/\x00#\x01\x00\x00#\x01\x00\x00\xb2\x02\x00\x00type@=dgb/rid@=9999/gid@=-9999/gfid@=824/gs@=1/uid@=13378067/nn@=\xe6\xbc\x86\xe9\xbb\x91\xe7\x9a\x84\xe9\xad\x85\xe5\xbd\xb1J/ic@=avatar@S013@S37@S80@S67_avatar/eid@=0/level@=24/dw@=0/gfcnt@=1/hits@=39/bcnt@=39/bst@=1/ct@=0/el@=/cm@=0/bnn@=\xe5\xb0\x8f\xe5\x83\xb5\xe5\xb0\xb8/bl@=12/brid@=9999/hc@=8ccfd113d28375263b0964c7221773bf/sahf@=0/fc@=0/gpf@=1/\x00\x1f\x01\x00\x00\x1f\x01\x00\x00\xb2\x02\x00\x00type@=dgb/rid@=9999/gid@=-9999/gfid@=824/gs@=1/uid@=23603518/nn@=\xe9\x82\xa3\xe5\xb9\xb4\xe7\x81\xac18\xe5\xb2\x81/ic@=avatar@S023@S60@S3'

danmu_regex = re.compile(b'txt@=(.+?)/cid@')
username_regex = re.compile(b'nn@=(.+?)/ic@')
level_regex = re.compile(b'level@=(.+?)/nl@')
card_regex = re.compile(b'bnn@=(.+?)/bl@')
card_level_regex = re.compile(b'bl@=(.+?)/brid@')

if __name__ =='__main__':
    print('aaa')
    danmu_username = username_regex.findall(data)
    danmu_content = danmu_regex.findall(data)
    danmu_level = level_regex.findall(data)
    danmu_card_level = card_level_regex.findall(data)
    danmu_card = card_regex.findall(data)
    print(danmu_username)
    for i in range(0,len(danmu_content)):
        print(danmu_content[i].decode('utf8'))
        print(danmu_username[i].decode('utf8'))

"""
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
    """