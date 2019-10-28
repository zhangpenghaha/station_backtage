import allure
import time
from selenium.webdriver.common.by import By

from station_backtage.base.base_action import BaseAction


class HomePage(BaseAction):

    # 切换站点
    select_station = By.ID, "headSelectStation"
    # 切换站点a标签
    select_station_a = By.XPATH, '//*[@id="headSelectStation"]/a'

    data_board =  By.XPATH,'//p[text()="数据看板"]'
    info_news = By.XPATH,'//p[text()="内容和信息"]'
    suk = By.XPATH,'//p[text()="服务SKU"]'
    business = By.XPATH,'//p[text()="商业管理"]'
    IOT = By.XPATH,'//p[text()="IOT管理"]'
    vip = By.XPATH,'//p[text()="会员管理"]'
    system_contral = By.XPATH,'//p[text()="系统管理"]'
    mall_contral = By.XPATH,'//p[text()="商城管理"]'

    # 点击数据看板
    @allure.step(title='点击数据看板')
    def click_data_board(self):
        return self.click(self.data_board)

    @allure.step(title='点击内容和信息')
    def click_info_news( self ):
        return self.click(self.info_news)

    @allure.step(title='点击服务SKU')
    def click_suk( self ):
        return self.click(self.suk)

    @allure.step(title='点击商业管理')
    def click_business( self ):
        return self.click(self.business)

    @allure.step(title='点击IOT管理')
    def click_IOT( self ):
        return self.click(self.IOT)

    @allure.step(title='点击会员管理')
    def click_vip( self ):
        return self.click(self.vip)

    @allure.step(title='点击系统管理')
    def click_system_contral( self ):
        return self.click(self.system_contral)

    @allure.step(title='点击商城管理')
    def click_mall_contral( self ):
        return self.click(self.mall_contral)

    @allure.step(title='获取数据看板文本')
    def get_text_data_board( self ):
        return self.get_text(self.data_board)

    @allure.step(title='获取内容和信息文本')
    def get_text_info_news( self ):
        return self.get_text(self.info_news)


    @allure.step(title='点击切换站点')
    def click_select_station( self ):
        return self.click(self.select_station)

    @allure.step(title='获取站点名')
    def get_text_station_name( self ):
        return self.get_text(self.select_station_a)

    @allure.step(title='选择具体火车站')
    def click_station_name(self, text):
        time.sleep(2)
        return self.click_div_text(text)
