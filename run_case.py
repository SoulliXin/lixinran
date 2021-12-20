# -*- codeing = utf-8 -*-
# @time : 2021/12/9 17:04
# @Author : LiXinRan
# @File : run_case.py
# @Software: PyCharm

import os
import unittest
import sys
from lib.HwTestReport import HTMLTestReportEN
import time

base_path = os.path.abspath(os.path.dirname(__file__)).split('util')[0]
sys.path.append(base_path)
case_path = base_path + '/case'
suit = unittest.TestSuite()
tests = unittest.defaultTestLoader.discover(case_path,'*.py')
suit.addTest(tests)
report_path = base_path + '/report' + "/ECShop_ATReport_" + time.strftime("%Y-%m-%d %H%M%S") + ".html"
report_AT = open(report_path,'wb')

runner = HTMLTestReportEN(stream=report_AT,title='ECshop自动化测试报告',description='本此概述如下：',verbosity=2,tester='LiXinRan')
res = runner.run(suit)
report_AT.close()


