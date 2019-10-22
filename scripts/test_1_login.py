import time
import allure
import pytest
from station_map_backstage.base.base_driver import InitDriver
from station_map_backstage.page.page import Page


class Test_station_news:

    @classmethod
    def setup_class(cls):
        cls.driver = InitDriver().get_driver()
        cls.page = Page(cls.driver)
        cls.driver.get("http://192.168.100.222/stationAdmin/start/#/user/login/msg=undefined")

    def setup(self):
        self.driver.get("http://192.168.100.222/stationAdmin/start/#/user/login/msg=undefined")

    def teardown(self):
        time.sleep(2)

    @classmethod
    def teardown_class(cls):
        time.sleep(2)
        # InitDriver().quit_driver()

    # @pytest.mark.order("10")
    # @pytest.mark.parametrize("args",read_excel("test_data.xlsx", ""))
    def test_add_station_news(self):
        # 输入用户名
        self.page.login.input_user_name("admin")
        # 输入密码
        self.page.login.input_pwd("123456")
        # 点击登录
        self.page.login.click_login()
        a1 = self.page.home.get_text_data_board()
        a2 = self.page.home.get_text_info_news()
        assert [a1, a2] == ["数据看板", "内容和信息"]

if __name__ == '__main__':
    import unittest

    unittest.main()