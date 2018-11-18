# coding=utf-8

import json
import os
import time
import pymysql
from selenium import webdriver


class MySql:
    def __init__(self):
        self.connection = self.connect()
        self.cursor = self.connection.cursor()

    def connect(self):
        return pymysql.Connect(host='localhost', port=3306, user='root', password='123456', db='dy_room_information',
                               charset='utf8')

    def insert(self, title, rid, anchor, watch_num, category):
        sql = 'insert into room (title, rid, anchor, watch_num, category) values(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');'.format(
            title, rid,
            anchor,
            watch_num,
            category)
        print(sql)
        self.cursor.execute(sql)
        self.connection.commit()
        print('成功插入房间号为{}的一条数据，目前共{}条'.format(rid, self.cursor.rowcount))

    def close(self):
        self.cursor.close()
        self.connection.close()


class DouYu(object):
    def __init__(self):
        self.start_url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()
        self.index = 1
        self.mysql = MySql()

    def get_content_list(self):  # 提取数据
        li_list = self.driver.find_elements_by_xpath('//ul[@id="live-list-contentbox"]/li')
        content_list = []
        for li in li_list:
            item = {'title': li.find_element_by_xpath('./a').get_attribute('title'),
                    'rid': li.find_element_by_xpath('./a').get_attribute('data-rid'),
                    'anchor': li.find_element_by_xpath('.//span[@class="dy-name ellipsis fl"]').text,
                    'watch_num': li.find_element_by_xpath('.//span[@class="dy-num fr"]').text,
                    'category': li.find_element_by_xpath('.//span[@class="tag ellipsis"]').text}
            print(item)
            content_list.append(item)
        # 提取下一页元素
        next_url = self.driver.find_elements_by_xpath('.//a[@class="shark-pager-next"]')
        next_url = next_url[0] if len(next_url) > 0 else None
        return content_list, next_url

    def save_content_list(self, content_list):
        js = "var q=document.documentElement.scrollTop=1000000"
        self.driver.execute_script(js)
        for li in content_list:
            self.mysql.insert(li['title'], int(li['rid']), li['anchor'], li['watch_num'], li['category'])
        # json_str = json.dumps(content_list, ensure_ascii=False, indent=4)
        # file_path = './douyu_{}page.json'.format(str(self.index))
        # is_exists = os.path.exists(file_path)
        # if not is_exists:
        #    os.system('touch {}'.format(file_path))
        # with open('./douyu_{}'.format(str(self.index)) + 'page.json', 'w', encoding='utf-8') as f:
        #    f.write(json_str)
        self.index += 1

    def run(self):  # 实现主要逻辑
        # start_url
        # 发送请求,获取响应
        self.driver.get(self.start_url)

        # 提取数据
        content_list, next_url = self.get_content_list()
        # 保存
        self.save_content_list(content_list)
        # 下一页数据的提取
        while next_url is not None:
            next_url.click()  # 页面没有完全加载完
            time.sleep(5)
            content_list, next_url = self.get_content_list()
            # 保存
            self.save_content_list(content_list)


if __name__ == '__main__':
    douyu = DouYu()
    douyu.run()
