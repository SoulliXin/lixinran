# -*- codeing = utf-8 -*-
# @time : 2021/12/2 10:02
# @Author : LiXinRan
# @File : find_element.py
# @Software: PyCharm
from util.read_ini import ReadIni

class FindElement:
    def __init__(self,driver):
        self.driver = driver


    def get_element(self,node,key):
        read_i = ReadIni()
        data = read_i.get_value(node,key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element_by_classNmae(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return None
