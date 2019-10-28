import allure
from selenium.webdriver.common.by import By

from station_backtage.base.base_action import BaseAction


class Business(BaseAction):

    # 站内商业
    station_business = By.LINK_TEXT, "站内商业"

    # 标题字段
    business_title = By.CLASS_NAME, "layui-table-cell"

    @allure.step(title="获取站内商业文本")
    def get_text_station_business( self ):
        return self.get_text(self.station_business)

    @allure.step(title="获取商业管理标题字段元素")
    def get_text_business_title(self):
        print(self.get_texts(self.business_title))
        return self.get_texts(self.business_title)