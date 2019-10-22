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
        cls.driver.get("http://192.168.100.222/stationAdmin/start/#/record/infor/infor")

    def setup(self):
        time.sleep(1)

    def teardown(self):
        allure.attach("截图", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)
        time.sleep(2)

    @classmethod
    def teardown_class(cls):
        time.sleep(2)
        # InitDriver().quit_driver()

    @pytest.mark.order("10")
    def test_data_board(self):
        # allure.attach("点击数据看板", allure.attach_type.TEXT)
        self.page.home.click_data_board()
        a1 = self.page.data_board.get_text_all_station()
        a2 = self.page.data_board.get_text_all_users()
        a3 = self.page.data_board.get_text_all_vip()
        assert [a1, a2, a3] == ["站点接入总量", "用户总量", "会员总量"]

    @pytest.mark.order("20")
    def test_info_news( self ):
        # allure.attach("点击内容和信息", allure.attach_type.TEXT)
        self.page.home.click_info_news()
        a1 = self.page.info_news.get_text_add_news()
        a2 = self.page.info_news.get_text_station_news()
        a3 = self.page.info_news.get_text_data_ollocate()
        assert [a1, a2, a3] == ["添加资讯", "车站资讯", "内容配置"]

    @pytest.mark.order("30")
    def test_sku( self ):
        # allure.attach("点击sku", allure.attach_type.TEXT)
        self.page.home.click_suk()
        a = self.page.sku.get_text_station_screen()
        assert a == "车站大屏"

    @pytest.mark.order("40")
    def test_business( self ):
        # allure.attach("点击商业管理", allure.attach_type.TEXT)
        self.page.home.click_business()
        a =self.page.business.get_text_station_business()
        assert a == "站内商业"

    @pytest.mark.order("50")
    def test_iot( self ):
        # allure.attach("点击IOT管理管理", allure.attach_type.TEXT)
        self.page.home.click_IOT()
        a1 = self.page.iot.get_text_overview()
        a2 = self.page.iot.get_text_papper_contral()
        a3 = self.page.iot.get_text_express_box()
        assert [a1, a2, a3] == ["概况", "纸巾机管理", "快递柜管理"]

    @pytest.mark.order("60")
    def test_vip( self ):
        # allure.attach("点击会员管理", allure.attach_type.TEXT)
        self.page.home.click_vip()
        a = self.page.vip.get_text_user_vip()
        assert a == "平台会员"

    @pytest.mark.order("70")
    def test_system_contral( self ):
        # allure.attach("点击系统管理", allure.attach_type.TEXT)
        self.page.home.click_system_contral()
        a1 = self.page.system_contral.get_text_users_contral()
        a2 = self.page.system_contral.get_text_role_contral()
        a3 = self.page.system_contral.get_text_menu_contral()
        assert [a1, a2, a3 ] == ["用户管理", "角色管理", "菜单管理"]

    @pytest.mark.order("80")
    def test_mall_contral( self ):
        # allure.attach("点击菜单管理", allure.attach_type.TEXT)
        self.page.home.click_mall_contral()
        a1 = self.page.mall_contral.get_text_goods_conrtal()
        a2 = self.page.mall_contral.get_text_order_contral()
        a3 = self.page.mall_contral.get_text_after_sale()
        assert [a1, a2, a3] == ["商品管理", "订单管理", "售后管理"]

    def test_select_station(self):
        self.page.home.click_select_station()
        self.page.home.click_station_name("罗山站")
        a1 = self.page.home.get_text_station_name()
        time.sleep(2)
        self.page.home.click_select_station()
        self.page.home.click_station_name("潜江站")
        a2 = self.page.home.get_text_station_name()
        time.sleep(2)
        self.page.home.click_select_station()
        self.page.home.click_station_name("武昌站")
        a3 = self.page.home.get_text_station_name()
        assert [a1, a2, a3] == ["罗山站", "潜江站", "武昌站"]


