import allure
from selenium.webdriver.common.by import By

from station_map_backstage.base.base_action import BaseAction


class Sku(BaseAction):

    # 车站大屏
    station_screen = By.LINK_TEXT, "车站大屏"
    # 标题字段
    sku_title = By.CLASS_NAME, "laytable-cell-numbers"

    @allure.step(title="获取车站大屏文本")
    def get_text_station_screen(self):
        return self.get_text(self.station_screen)

