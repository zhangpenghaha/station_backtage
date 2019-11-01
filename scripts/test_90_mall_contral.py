import time
import allure
import pytest
from station_backtage.base.base_driver import InitDriver
from station_backtage.page.page import Page


class Test_Mall_Contral:

    @classmethod
    def setup_class(cls):
        cls.driver = InitDriver().get_driver()
        cls.page = Page(cls.driver)
        cls.driver.get("http://192.168.100.222/stationAdmin/start/#/mall/product/productList")

    def setup(self):
        self.driver.get("http://192.168.100.222/stationAdmin/start/#/mall/product/productList")

    def teardown(self):
        time.sleep(2)

    @classmethod
    def teardown_class(cls):
        time.sleep(5)
        InitDriver().quit_driver()

    @pytest.mark.order("10")
    # @pytest.mark.parametrize("args",read_excel("test_data.xlsx", ""))
    def test_goods_contral( self ):
        # self.page.mall_contral.click_goods_conrtal()
        a = self.page.mall_contral_goods_contral.get_text_add_goods()
        assert a == "添加商品"

    def test_order_contral_texts(self):
        self.page.mall_contral.click_order_contral()
        a = self.page.mall_contral_order_contral.get_text_order_contral()
        print(a)
        assert a == ["订单编号", "收货人", "下单时间", "商家", "站", "局"]