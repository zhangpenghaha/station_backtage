import allure
from selenium.webdriver.common.by import By

from station_backtage.base.base_action import BaseAction


class Vip(BaseAction):

    # 平台会员
    user_vip = By.LINK_TEXT, "平台会员"
    # 标题字段
    sku_title = By.CLASS_NAME, "laytable-cell-numbers"

    @allure.step(title="获取平台会员文本")
    def get_text_user_vip(self):
        return self.get_text(self.user_vip)