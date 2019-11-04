import allure
from selenium.webdriver.common.by import By
from station_backtage.base.base_action import BaseAction


class MallContralOrderContral(BaseAction):

    # 添加商品
    order_texts = By.CLASS_NAME, "layui-form-labelv2"
    # 商品名称
    goods_name = By.XPATH, '//*[@id="LAY_app_body"]/div[2]/div[1]/div/div/div[1]/div/input'
    # 商品状态
    goods_status = By.XPATH, "*//select"
    # 添加人账号
    add_name = By.NAME, "createBy"
    # 开始时间
    start_time = By.ID, "startTime"
    # 结束时间
    end_time = By.ID, "endTime"


    @allure.step(title="获取添加商品文本")
    def get_text_order_contral( self ):
        return self.get_texts(self.order_texts)