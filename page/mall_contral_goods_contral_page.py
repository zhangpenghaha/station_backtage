import allure
from selenium.webdriver.common.by import By
from station_backtage.base.base_action import BaseAction


class MallContralGoodsContral(BaseAction):

    # 查询
    btn_search = By.ID, "search-btn"
    # 添加商品
    btn_add_goods = By.LINK_TEXT, "添加商品"

    @allure.step(title="获取添加商品文本")
    def get_text_add_goods( self ):
        return self.get_text(self.btn_add_goods)


