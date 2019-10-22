import allure
from selenium.webdriver.common.by import By

from station_map_backstage.base.base_action import BaseAction


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