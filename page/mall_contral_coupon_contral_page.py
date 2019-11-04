import allure
from selenium.webdriver.common.by import By
from station_backtage.base.base_action import BaseAction


class MallContralCouponContral(BaseAction):

    # 优惠券类型
    coupon_type = By.XPATH, '*//label[text()="优惠券类型："]'

    @allure.step(title="获取优惠券类型文本")
    def get_text_coupon_type( self ):
        return self.get_text(self.coupon_type)