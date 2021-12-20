# -*- codeing = utf-8 -*-
# @time : 2021/12/9 14:48
# @Author : LiXinRan
# @File : ddt_01register_case.py
# @Software: PyCharm
from selenium import webdriver
import time
import unittest
from business.register_business import RegisterBusiness
import ddt
from util.excel_util import ExcelUtil
import os


ex = ExcelUtil()
data = ex.get_data()



@ddt.ddt
class Register_case(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get('http://192.168.226.138/index.php')
        self.driver.maximize_window()
        self.register = RegisterBusiness(self.driver)

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
    def test_register_case_(self,data):
        testcase,info,username,email,password,confpass,msn,qq,worktelp,famtelp,telphone,answer=data
        rejust = self.register.register_(testcase,info,username,email,password,confpass,msn,qq,worktelp,famtelp,telphone,answer)
        self.assertTrue(rejust,'Testfail')
