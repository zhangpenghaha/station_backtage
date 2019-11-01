import allure
from selenium.webdriver.common.by import By
from station_backtage.base.base_action import BaseAction


class MallContralGoodsContral(BaseAction):

    # 商品管理明细字段
    goods_texts = By.XPATH, '//div[@class="layui-table-header"]//span'

    # 商品状态
    goods_status = By.CLASS_NAME, "layui-input layui-unselect"

    # 查询
    btn_search = By.ID, "search-btn"

    # 添加商品
    btn_add_goods = By.LINK_TEXT, "添加商品"

    @allure.step(title="获取添加商品文本")
    def get_text_add_goods( self ):
        return self.get_text(self.btn_add_goods)

    def get_text_goods_texts(self):
        a = self.find_elements(self.goods_texts)
        list_text = []
        for i in a:
            i.text()
            list_text.append(list_text)
        print(list_text)

