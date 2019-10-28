import time
import allure
import pytest
from station_backtage.base.base_driver import InitDriver
from station_backtage.page.page import Page


class TestInfoNews:

    @classmethod
    def setup_class(cls):
        cls.driver = InitDriver().get_driver()
        cls.page = Page(cls.driver)
        cls.driver.get("http://192.168.100.222/stationAdmin/start/#/info/news/news")

    def setup(self):
        self.driver.get("http://192.168.100.222/stationAdmin/start/#/info/news/news")

    def teardown(self):
        time.sleep(2)

    @classmethod
    def teardown_class(cls):
        time.sleep(5)
        InitDriver().quit_driver()

    @pytest.mark.order("10")
    # @pytest.mark.parametrize("args",read_excel("test_data.xlsx", ""))
    def test_info_news(self):
        # allure.attach("测试标题",args[10], allure.attach_type.TEXT)
        a = self.page.info_news.get_text_add_news()
        assert a == "添加资讯"


if __name__ == '__main__':
    import unittest

    unittest.main()