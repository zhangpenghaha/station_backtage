import allure
from selenium.webdriver.common.by import By

from station_backtage.base.base_action import BaseAction


class SystemContral(BaseAction):

    # 用户管理
    users_contral = By.LINK_TEXT, "用户管理"
    # 角色管理
    role_contral = By.LINK_TEXT, "角色管理"
    # 菜单管理
    menu_contral = By.LINK_TEXT, "菜单管理"

    @allure.step(title="获取用户管理文本")
    def get_text_users_contral(self):
        return self.get_text(self.users_contral)

    @allure.step(title="获取角色管理文本")
    def get_text_role_contral( self ):
        return self.get_text(self.role_contral)

    @allure.step(title="获取菜单管理文本")
    def get_text_menu_contral( self ):
        return self.get_text(self.menu_contral)