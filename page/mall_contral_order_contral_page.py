import allure
from selenium.webdriver.common.by import By
from station_backtage.base.base_action import BaseAction


class MallContralOrderContral(BaseAction):

    order_texts = By.CLASS_NAME, "layui-form-labelv2"

    @allure.step(title="获取添加商品文本")
    def get_text_order_contral( self ):
        return self.get_texts(self.order_texts)