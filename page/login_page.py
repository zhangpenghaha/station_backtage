import allure
from selenium.webdriver.common.by import By

from station_backtage.base.base_action import BaseAction
import time
import allure
import pytest

from station_backtage.base.base_driver import InitDriver


class Login(BaseAction):


    # 账户名
    user_name = By.ID, "LAY-user-login-username"

    # 密码
    password = By.ID, "LAY-user-login-password"

    # 登录
    btn_login = By.ID, "login-submit"

    # 输入用户名
    @allure.step(title='输入用户名')
    def input_user_name(self, text):
        return self.input(self.user_name, text)

    # 输入密码
    @allure.step(title='输入密码')
    def input_pwd(self, text):
        return self.input(self.password, text)

    # 点击登录
    @allure.step(title='点击登录')
    def click_login(self):
        return self.click(self.btn_login)

    def login(self):
        driver = InitDriver().get_driver()
        driver.get("http://192.168.100.222/stationAdmin/start/#/user/login/msg=undefined")
        # 输入用户名
        driver.find_element_by_id("LAY-user-login-username").send_keys("admin")
        # 输入密码
        driver.find_element_by_id("LAY-user-login-password").send_keys("123456")
        # 点击登录
        driver.find_element_by_id("login-submit").click()

if __name__ == '__main__':
    Login(BaseAction).login()