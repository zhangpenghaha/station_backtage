import allure
from selenium.webdriver.common.by import By

from station_backtage.base.base_action import BaseAction


class InfoNews(BaseAction):

    # 车站咨询
    add_news = By.LINK_TEXT, "添加资讯"

    station_news = By.LINK_TEXT, "车站资讯"

    data_collocate = By.LINK_TEXT, "内容配置"

    notify = By.LINK_TEXT, "公告管理"

    @allure.step(title='获取添加资讯文本')
    def get_text_add_news(self):
        return self.get_text(self.add_news)

    @allure.step(title='获取车站资讯文本')
    def get_text_station_news( self ):
        return self.get_text(self.station_news)

    @allure.step(title='获取内容配置文本')
    def get_text_data_ollocate( self ):
        return self.get_text(self.data_collocate)

    @allure.step(title='获取公告管理文本')
    def get_text_notify( self ):
        return self.get_text(self.notify)





















    # # 业务参数设置
    # ywcssz = By.CLASS_NAME, 'el-submenu__title'
    # # 国际配置
    # gjpz = By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/ul/li[1]/ul/li[1]'
    # # 本地IP
    # bd_ip = By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div/input'
    # # 本地活动端口
    # bd_port = By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/input'
    # # SIP服务器ID
    # sip_id = By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[3]/div/div/input'
    # # SIP服务器域
    # sip_fwqy = By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[4]/div/div/input'
    # # SIP服务器地址
    # sip_fwqdz = By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[5]/div/div/input'
    # # SIP服务器端口
    # sip_fwqdk = By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[6]/div/div/input'
    # # SIP用户名
    # sip_username = By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[7]/div/div/input'
    # # SIP用户认证ID
    # sip_user_id = By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[8]/div/div/input'
    # # 密码
    # password = By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div[2]/form/div[9]/div/div/input'
    # # 保存
    # gjpz_save = By.CLASS_NAME, 'el-button--primary'
    # # 重置
    # gjpz_reset = By.CLASS_NAME, 'el-button--default'
    # # 弹框
    # el_message = By.CLASS_NAME, "el-message__content"
    #
    # @allure.step(title='点击国际配置')
    # def click_gjbp(self):
    #     try:
    #         self.click(self.gjpz)
    #     except:
    #         self.click(self.ywcssz)
    #         self.click(self.gjpz)
    #
    #
    # @allure.step(title='输入本地IP')
    # def input_bd_ip(self, text):
    #     allure.attach("输入本地IP", text, allure.attach_type.TEXT)
    #     self.input(self.bd_ip, text)
    #
    # @allure.step(title='输入本地活动端口')
    # def input_bd_port(self, text):
    #     allure.attach("输入本地活动端口", text, allure.attach_type.TEXT)
    #     self.input(self.bd_port, text)
    #
    # @allure.step(title='输入SIP服务器ID')
    # def input_sip_id(self, text):
    #     allure.attach("输入SIP服务器ID", text, allure.attach_type.TEXT)
    #     self.input(self.sip_id, text)
    #
    # @allure.step(title='输入SIP服务器域')
    # def input_sip_fwqy(self, text):
    #     allure.attach("输入SIP服务器域", text, allure.attach_type.TEXT)
    #     self.input(self.sip_fwqy, text)
    #
    # @allure.step(title='输入SIP服务器地址')
    # def input_sip_fwqdz(self, text):
    #     allure.attach("输入SIP服务器地址", text, allure.attach_type.TEXT)
    #     self.input(self.sip_fwqdz, text)
    #
    # @allure.step(title='输入SIP服务器端口')
    # def input_sip_fwqdk(self, text):
    #     allure.attach("输入SIP服务器端口", text, allure.attach_type.TEXT)
    #     self.input(self.sip_fwqdk, text)
    #
    # @allure.step(title='输入SIP用户名')
    # def input_sip_username(self, text):
    #     allure.attach("输入SIP用户名", text, allure.attach_type.TEXT)
    #     self.input(self.sip_username, text)
    #
    # @allure.step(title='输入SIP用户认证ID')
    # def input_sip_user_id(self, text):
    #     allure.attach("输入SIP用户认证ID", text, allure.attach_type.TEXT)
    #     self.input(self.sip_user_id, text)
    #
    # @allure.step(title='输入密码')
    # def input_password(self, text):
    #     allure.attach("输入密码", text, allure.attach_type.TEXT)
    #     self.input(self.password, text)
    #
    # @allure.step(title='点击国际配置的保存')
    # def click_gjpz_save(self):
    #     allure.attach("截图", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)
    #     self.click(self.gjpz_save)
    #
    # @allure.step(title='点击重置')
    # def click_gjpz_reset(self):
    #     self.click(self.gjpz_reset)
    #
    #
    # @allure.step(title='获取弹框信息')
    # def get_el_message(self):
    #     return self.get_text(self.el_message)