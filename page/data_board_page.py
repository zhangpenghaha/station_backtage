import allure
from selenium.webdriver.common.by import By

from station_backtage.base.base_action import BaseAction


class DataBoard(BaseAction):


    # 概况

    # 车站通数据统计
    # 车站通站点数据统计
    # 纸巾机数据统计
    # 寄存柜数据统计
    # 指路机数据统计
    # 公众号数据统计
    # 问卷数据统计


    # 站点接入总量
    all_station = By.XPATH,'//div[text()="站点接入总量"]'

    #用户总量
    all_users = By.XPATH,'//div[text()="用户总量"]'

    # 会员总量
    all_vip = By.XPATH,'//div[text()="会员总量"]'

    @allure.step(title='获取站点接入总量文本')
    def get_text_all_station(self):
       return self.get_text(self.all_station)

    @allure.step(title='获取用户总量文本')
    def get_text_all_users( self ):
        return self.get_text(self.all_users)

    @allure.step(title='获取会员总量文本')
    def get_text_all_vip( self ):
        return self.get_text(self.all_vip)