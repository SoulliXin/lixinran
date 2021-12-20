# -*- codeing = utf-8 -*-
# @time : 2021/12/2 14:37
# @Author : LiXinRan
# @File : register_business.py
# @Software: PyCharm
from selenium import webdriver
from handle.Register_handle import RegisterHandle
from handle.Register_handle import LoginHandle
import time
class RegisterBusiness:
    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)

    def user_register(self,username,email,password,confpass,msn,qq,worktelp,famtelp,telphone,answer):
        self.register_h.click_register()
        self.register_h.send_username(username)
        self.register_h.send_email(email)
        self.register_h.send_password(password)
        self.register_h.send_confirmpass(confpass)
        self.register_h.send_MSN(msn)
        self.register_h.send_qq(qq)
        self.register_h.send_worktelp(worktelp)
        self.register_h.send_famtelp(famtelp)
        self.register_h.send_telphone(telphone)
        # self.register_h.get_select_buttun_()
        # time.sleep(2)
        self.register_h.select_buttun()
        self.register_h.send_answer(answer)
        # self.register_h.commit()
        # time.sleep(2)


    # def register_error(self,username,email,password,confpass,msn,qq,worktelp,famtelp,telphone,answer,info):
    #     if info == 'suc_register':
    #         self.user_register(username,email,password,confpass,msn,qq,worktelp,famtelp,telphone,answer)
    #         self.register_h.commit()
    #     if self.register_h.get_register_text(info) in '- 用户名长度不能少于 3 个字符。' or '* 用户名已经存在,请重新输入':
    #         return True
    #     elif self.register_h.get_register_text(info) in '* 邮件地址不合法' or '* 邮箱已存在,请重新输入':
    #         return True
    #     elif self.register_h.get_register_text(info) in '- 登录密码不能少于 6 个字符。':
    #         return True
    #     elif self.register_h.get_register_text(info) in '- 登录密码不能少于 6 个字符。':
    #         return True
    #     else:
    #         return False

    def register_(self,testcase,info,username,email,password,confpass,msn,qq,worktelp,famtelp,telphone,answer):
        if info == 'suc_register':
            self.user_register(username,email,password,confpass,msn,qq,worktelp,famtelp,telphone,answer)
            self.register_h.commit()
            text = self.register_h.get_register_text(info)
            if text:
                return True
            else:
                return False
        else:
            self.user_register(username, email, password, confpass, msn, qq, worktelp, famtelp, telphone, answer)
            if self.register_h.get_register_text(info) in '- 用户名长度不能少于 3 个字符。' or '* 用户名已经存在,请重新输入':
                return True
            elif self.register_h.get_register_text(info) in '* 邮件地址不合法' or '* 邮箱已存在,请重新输入':
                return True
            elif self.register_h.get_register_text(info) in '- 登录密码不能少于 6 个字符。':
                return True
            elif self.register_h.get_register_text(info) in '- 登录密码不能少于 6 个字符。':
                return True
            else:
                return False

class Login_business:

    def __init__(self,driver):
        self.login_h =  LoginHandle(driver)

    def user_login(self,user,pas):
        self.login_h.click_login_buttun()
        self.login_h.send_user(user)
        self.login_h.send_pass(pas)
        self.login_h.comit_login()


    def login_(self,info,user,pas):
        self.user_login(user, pas)
        if info == 'succ_loin':
            text = self.login_h.get_succ_login_text(info)
            if text:
                return True
            else:
                return False
        elif info == 'error_user':
            text = self.login_h.get_succ_login_text(info)
            if text:
                return False
            else:
                return True
        elif info == 'error_pas':
            text = self.login_h.get_succ_login_text(info)
            if text:
                return False
            else:
                return True