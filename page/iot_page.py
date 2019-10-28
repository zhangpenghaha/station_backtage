import allure
from selenium.webdriver.common.by import By

from station_backtage.base.base_action import BaseAction


class Iot(BaseAction):

    # 概况
    overview = By.LINK_TEXT, "概况"
    # 纸巾机管理
    papper_contral = By.LINK_TEXT, "纸巾机管理"
    # 快递柜管理
    express_box = By.LINK_TEXT, "快递柜管理"

    @allure.step(title="获取概况文本")
    def get_text_overview(self):
        return self.get_text(self.overview)

    @allure.step(title="获取纸巾机管理文本")
    def get_text_papper_contral( self ):
        return self.get_text(self.papper_contral)

    @allure.step(title="获取快递柜管理文本")
    def get_text_express_box( self ):
        return self.get_text(self.express_box)
