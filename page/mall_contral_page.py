import allure
from selenium.webdriver.common.by import By
from station_backtage.base.base_action import BaseAction
class MallContral(BaseAction):

    # 商品管理
    goods_conrtal = By.LINK_TEXT, "商品管理"
    # 订单管理
    order_contral = By.LINK_TEXT, "订单管理"
    # 售后管理
    after_sale = By.LINK_TEXT, "售后管理"
    # 优惠券管理
    coupon_contral  = By.LINK_TEXT, "优惠券管理"
    # 会员管理
    vip_contral = By.LINK_TEXT, "会员管理"

    @allure.step(title="获取商品管理文本")
    def get_text_goods_conrtal(self):
        return self.get_text(self.goods_conrtal)

    @allure.step(title="获取订单管理文本")
    def get_text_order_contral( self ):
        return self.get_text(self.order_contral)

    @allure.step(title="获取售后管理文本")
    def get_text_after_sale( self ):
        return self.get_text(self.after_sale)

    @allure.step(title="点击商品管理")
    def click_goods_conrtal( self ):
        return self.click(self.goods_conrtal)

    @allure.step(title="点击订单管理")
    def click_order_contral( self ):
        return self.click(self.order_contral)

    @allure.step(title="点击售后管理")
    def click_after_sale( self ):
        return self.click(self.after_sale)

    @allure.step(title="点击优惠券管理")
    def click_coupon_contral( self ):
        return self.click(self.coupon_contral)

    @allure.step(title="点击会员管理")
    def click_vip_contral( self ):
        return self.click(self.vip_contral)

    

