# 使用自定义的 pymysql 工具类
import time
import unittest
from parameterized import parameterized
from station_backtage.base.base_excel import read_excel
from station_backtage.base.base_mysql import DBUtil

class TestLogin(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        cls.mysql_data  = DBUtil( "wt_bigdata")
        print(1)

    def setup(self):
        print("____________________________________________________________")

    @classmethod
    def teardown_class(cls):
        time.sleep(2)

    @parameterized.expand(read_excel("test_data.xlsx", "page"))
    def test(self, args):
        args = str(args)
        sql1 = 'select page_name from buried_point where page_name="{}"'.format(args)
        rows = self.mysql_data.get_sql(sql1)
        time.sleep(1)
        try:
            print(rows[0][0])
            assert str(rows[0][0]) == args
        except:
            assert 0

    @parameterized.expand(read_excel("test_data.xlsx", "huiyuan"))
    def test( self, args ):
        args = str(args)
        sql1 = 'select element_id from buried_point where element_id="{}"'.format(args)
        rows = self.mysql_data.get_sql(sql1)
        print(rows[0][0])
        try:
            assert str(rows[0][0]) == args
        except IndexError:
            return False


    def teardown(self):
        pass




