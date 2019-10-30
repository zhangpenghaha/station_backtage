from station_backtage.page.business_page import Business
from station_backtage.page.data_board_page import DataBoard
from station_backtage.page.home_page import HomePage
from station_backtage.page.iot_page import Iot
from station_backtage.page.login_page import Login
from station_backtage.page.info_news_page import InfoNews
from station_backtage.page.mall_contral_goods_contral_page import MallContralGoodsContral
from station_backtage.page.mall_contral_order_contral_page import MallContralOrderContral
from station_backtage.page.mall_contral_page import MallContral
from station_backtage.page.sku_page import Sku
from station_backtage.page.system_contral_page import SystemContral
from station_backtage.page.vip_page import Vip


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def info_news(self):
        """内容与信息"""
        return InfoNews(self.driver)


    @property
    def login( self ):
        """登录"""
        return Login(self.driver)

    @property
    def home( self ):
        """首页"""
        return HomePage(self.driver)

    @property
    def data_board( self ):
        """数据看板"""
        return DataBoard(self.driver)

    @property
    def sku( self ):
        """服务SKU"""
        return Sku(self.driver)

    @property
    def business( self ):
        """商业管理"""
        return Business(self.driver)

    @property
    def iot( self ):
        """IOT管理"""
        return Iot(self.driver)

    @property
    def vip( self ):
        """会员管理"""
        return Vip(self.driver)

    @property
    def mall_contral( self ):
        """商城管理"""
        return MallContral(self.driver)

    @property
    def system_contral( self ):
        """系统管理"""
        return SystemContral(self.driver)

    # MallContralGoodsContral 商城管理-商品管理
    @property
    def mall_contral_goods_contral( self ):
        """商品管理"""
        return MallContralGoodsContral(self.driver)

    # MallContralOrderContral 商城管理-订单管理
    def mall_contral_order_contral(self):
        return MallContralOrderContral(self.driver)