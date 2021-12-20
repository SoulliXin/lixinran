# -*- codeing = utf-8 -*-
# @time : 2021/12/10 9:30
# @Author : LiXinRan
# @File : ddt_02login_case.py
# @Software: PyCharm

from selenium import webdriver
import time
import unittest
from business.register_business import Login_business
import ddt
from util.excel_util import ExcelUtil
import os
ex = ExcelUtil('c:/ECshopUItest/config/case.xlsx', 1)
data = ex.get_data()

@ddt.ddt
class Loging_case(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get('http://192.168.226.138/index.php')
        self.driver.maximize_window()
        self.register = Login_business(self.driver)

    def tearDown(self) -> None:
        time.sleep(2)
        # if sys.exc_info()[0]:
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd() + "/report/" + case_name + ".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()

    @ddt.data(*data)
    def test_login_case_(self,data):
        testcase,info,user,pas=data
        rejust = self.register.login_(info,user,pas)
        self.assertTrue(rejust,'Testfail')