# -*- codeing = utf-8 -*-
# @time : 2021/12/2 11:47
# @Author : LiXinRan
# @File : Register_handle.py
# @Software: PyCharm
from page.Register_page import RegisterPage
from page.Register_page import LogingPage
from log.user_log import Logs_
import time

class RegisterHandle:
    def __init__(self,driver):
        self.register_p = RegisterPage(driver)
        gl = Logs_()
        self.get_logs = gl.get_log()





    def click_register(self):
        '''
        点击注册按钮
        '''
        self.register_p.get_registerbuttun().click()

    def send_username(self,username):
        '''
        输入用户名
        '''
        username = str(username)
        self.get_logs.info("输入用户名：" + username)
        self.register_p.get_username_element().send_keys(username)

    def send_email(self,email):
        '''
        输入电子邮件
        '''
        email = str(email)
        self.get_logs.info("输入邮箱：" + email)
        self.register_p.get_email_element().send_keys(email)

    def send_password(self,password):
        '''
        输入密码
        '''
        password = str(password)
        self.get_logs.info("输入密码：" + password)
        self.register_p.get_password_element().send_keys(password)

    def send_confirmpass(self,confpass):
        '''
        确认密码
        '''
        confpass = str(confpass)
        self.get_logs.info("输入确认密码：" + confpass)
        self.register_p.get_confirmpass_element().send_keys(confpass)

    def send_MSN(self,msn):
        '''
        输入MSN
        '''
        msn = str(msn)
        self.get_logs.info("输入msn：" + msn)
        self.register_p.get_msn_element().send_keys(msn)

    def send_qq(self,qq):
        '''
        输入QQ
        '''
        qq = str(qq)
        self.get_logs.info("输入qq：" + qq)
        self.register_p.get_QQ_element().send_keys(qq)

    def send_worktelp(self,worktelp):
        '''
        输入办公电话
        '''
        worktelp = str(worktelp)
        self.get_logs.info("输入办公电话：" + worktelp)
        self.register_p.get_wordtlp_element().send_keys(worktelp)

    def send_famtelp(self,famtelp):
        '''
        输入家庭电话
        '''
        famtelp = str(famtelp)
        self.get_logs.info("输入家庭电话：" + famtelp)
        self.register_p.get_fmtl_element().send_keys(famtelp)

    def send_telphone(self,telphone):
        '''
        输入手机号
        '''
        telphone = str(telphone)
        self.get_logs.info("输入手机号：" + telphone)
        self.register_p.get_telphone_element().send_keys(telphone)

    # def get_select_buttun_(self):
    #     '''
    #     获取下拉框按钮点击
    #     '''
    #     self.register_p.get_registerbuttun().click()
    #     time.sleep(1)


    def select_buttun(self):
        '''
        选择下拉框
        '''
        self.register_p.get_selectqs_element().click()

    def send_answer(self,answer):
        '''
        输入密码提示问题
        '''
        answer = str(answer)
        self.get_logs.info("输入密码提示：" + answer)
        self.register_p.get_answer_element().send_keys(answer)

    def commit(self):
        '''
        点击注册
        '''
        self.register_p.get_submit_element().click()

    def get_register_suc_text(self):
        self.register_p.get_register_succsess_element()

    def get_current_url(self):
        self.register_p.get_url()


    def get_register_text(self,info):
            if info == 'error_username' or 'repite_username':
                text = self.register_p.get_usernametext_element().text
            elif info == 'error_email' or 'repite_email':
                text = self. register_p.get_emailtext_element().text
            elif info == 'error_password':
                text = self.register_p.get_passwordtext_element().text
            elif info == 'error_confirmpassword':
                text = self.register_p.get_confirmpasstext_element().text
            elif info == 'suc_register':
                text = self.register_p.get_register_succsess_element().text
            else:
                return None
            return text



class LoginHandle:
    def __init__(self,driver):
        self.loging_p = LogingPage(driver)
        self.logger = Logs_().get_log()

    def click_login_buttun(self):
        self.loging_p.get_clicklogin_element().click()

    def send_user(self,user):
        user = str(user)
        self.logger.info("输入用户名：" + user)
        self.loging_p.get_user_element().send_keys(user)

    def send_pass(self,pas):
        pas = str(pas)
        self.logger.info("输入密码：" + pas)
        self.loging_p.get_pass_element().send_keys(pas)

    def comit_login(self):
        self.loging_p.get_loging_buttun_element().click()

    def get_succ_login_text(self,info):
        if info == 'succ_loin' or 'error_pass' or 'error_user':
            text = self.loging_p.get_succ_login_element()
            return text


class ShoppingHandle:
    pass