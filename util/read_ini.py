# -*- codeing = utf-8 -*-
# @time : 2021/12/2 10:04
# @Author : LiXinRan
# @File : read_ini.py
# @Software: PyCharm
import configparser
class ReadIni:
    def __init__(self,file_name=None,node=None):
        if file_name == None:
            self.file_name = 'c:/ECshopUItest/config/Location_element.ini'
        if node == None:
            self.node = 'RegisterElement'
        else:
            self.node = node
        self.cf = self.load_ini(self.file_name)


    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf


    def get_value(self,node,key):
        data = self.cf.get(node,key)
        return data

if __name__ == '__main__':
    ini = ReadIni()
    data = ini.get_value('LoginElement','user')
    print(data)






