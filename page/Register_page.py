# -*- codeing = utf-8 -*-
# @time : 2021/12/2 11:25
# @Author : LiXinRan
# @File : Register_page.py
# @Software: PyCharm
from base.find_element import FindElement

class RegisterPage:
    def __init__(self,driver):
        self.fd = FindElement(driver)
        self.driver = driver
    #获取用户名元素
    def get_username_element(self):
        return self.fd.get_element('RegisterElement','user_name')
    #获取用户邮箱元素
    def get_email_element(self):
        return self.fd.get_element('RegisterElement','user_email')

    # 获取用户密码元素
    def get_password_element(self):
        return self.fd.get_element('RegisterElement','user_password')

    # 获取确认密码元素
    def get_confirmpass_element(self):
        return self.fd.get_element('RegisterElement','confirm_password')

    # 获取msn元素
    def get_msn_element(self):
        return self.fd.get_element('RegisterElement','user_MSN')

    # 获取qq元素
    def get_QQ_element(self):
        return self.fd.get_element('RegisterElement','user_qq')

    # 获取工作电话元素
    def get_wordtlp_element(self):
        return self.fd.get_element('RegisterElement','work_telphone')

    # 获取家庭电话元素
    def get_fmtl_element(self):
        return self.fd.get_element('RegisterElement','home_telphone')
    # 获取手机元素
    def get_telphone_element(self):
        return self.fd.get_element('RegisterElement','tel_phone')

    # #获取下拉框按钮
    # def get_select_buttun(self):
    #
    #     return self.fd.get_element('RegisterElement','select_buttun')

    # 获取下拉框示元素
    def get_selectqs_element(self):
        return self.fd.get_element('RegisterElement','select_qustion')

    # 获取密码提示元素
    def get_answer_element(self):
        return self.fd.get_element('RegisterElement','pass_answer')

    # 获注册元素
    def get_submit_element(self):
        return self.fd.get_element('RegisterElement','register_submit')
    # 获取点击注册按钮元素
    def get_registerbuttun(self):
        return self.fd.get_element('RegisterElement','register_buttun')

    # 获取用户文字名元素
    def get_usernametext_element(self):
        return self.fd.get_element('RegisterElement','error_username')

    # 获取邮箱文字元素
    def get_emailtext_element(self):
        return self.fd.get_element('RegisterElement','error_email')
    # 获取密码文字元素

    def get_passwordtext_element(self):
        return self.fd.get_element('RegisterElement','error_password')
    # 获取确认密码文字元素
    def get_confirmpasstext_element(self):
        return self.fd.get_element('RegisterElement','error_confirmpassword')

    def get_register_succsess_element(self):
        return self.fd.get_element('RegisterElement','register_succsess_element')

    def get_url(self):
        return self.driver.current_url

class LogingPage:
    def __init__(self,driver):
        self.fd = FindElement(driver)

    def get_clicklogin_element(self):
        return self.fd.get_element('LoginElement','login_buttun')

    def get_user_element(self):
        return self.fd.get_element('LoginElement','user')

    def get_pass_element(self):
        return self.fd.get_element('LoginElement','pass')

    def get_loging_buttun_element(self):
        return self.fd.get_element('LoginElement','loging_comit')

    def get_succ_login_element(self):
        return self.fd.get_element('LoginElement', 'loging_success')



class ShoppingPage:
    def __init__(self, driver):
        self.fd = FindElement(driver)
    def get_serch_element(self):
        return self.fd.get_element('Shoppingelement','serch_input')
    def get_serch_buttun_element(self):
        return self.fd.get_element('Shoppingelement','serch_buttun')
    def get_shop_trolley_element(self):
        return self.fd.get_element('Shoppingelement','shop_trolley')
    def get_telphonegoods_element(self):
        return self.fd.get_element('Shoppingelement','telphone_good')
    def get_account_element(self):
        return self.fd.get_element('Shoppingelement','close_account')
    def get_arer_element(self):
        return self.fd.get_element('Shoppingelement','Distribution_area')
    def get_ciyt_area_element(self):
        return self.fd.get_element('Shoppingelement','city_area')
    def get_part_area_element(self):
        return self.fd.get_element('Shoppingelement','part_area')
    def get_consignee_name_element(self):
        return self.fd.get_element('Shoppingelement','consignee_name')
    def get_address_element(self):
        return self.fd.get_element('Shoppingelement','address')
    def get_tel_element(self):
        return self.fd.get_element('Shoppingelement','tel')
    def get_address_butten_element(self):
        return self.fd.get_element('Shoppingelement','address_butten')
    def get_select_send_way_element(self):
        return self.fd.get_element('Shoppingelement','select_send_way')
    def get_select_pay_way_element(self):
        return self.fd.get_element('Shoppingelement','select_pay_way')
    def get_commit_element(self):
        return self.fd.get_element('Shoppingelement','commit')