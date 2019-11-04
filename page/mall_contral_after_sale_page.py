import allure
from selenium.webdriver.common.by import By
from station_backtage.base.base_action import BaseAction


class MallContralAfterSale(BaseAction):

    # 售后管理
    text_after_sale = By.XPATH, '*//cite[text()="售后管理"]'
    # 商品管理明细字段
    goods_texts = By.XPATH, '//div[@class="layui-table-header"]//span'

    # 商品状态
    goods_status = By.CLASS_NAME, "layui-input layui-unselect"
    # 待上架
    select_shelf = By.XPATH, '*//div[@class="layui-input-block"]//dd[text()="待上架"]'
    # 销售中
    select_sale = By.XPATH, '*//div[@class="layui-input-block"]//dd[text()="销售中"]'
    # 已售罄
    select_sold_out = By.XPATH, '*//div[@class="layui-input-block"]//dd[text()="已售罄"]'
    # 已下架
    select_have_obtained = By.XPATH, '*//div[@class="layui-input-block"]//dd[text()="已下架"]'

    # 查询
    btn_search = By.ID, "search-btn"

    # 添加商品
    btn_add_goods = By.LINK_TEXT, "添加商品"
    # 上架
    btn_shelf = By.XPATH, '*//button[text()="上架"]'
    # 下架
    btn_obtained = By.XPATH, '*//button[text()="下架"]'
    # 查看
    btn_check = By.LINK_TEXT, "查看"
    # 修改
    btn_revamp = By.LINK_TEXT, "修改"

    @allure.step(title="获取售后管理文本")
    def get_text_after_sale( self ):
        return self.get_text(self.text_after_sale)