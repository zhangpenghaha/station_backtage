# 使用自定义的 pymysql 工具类
import time
import unittest
from parameterized import parameterized
from station_backtage.base.base_excel import read_excel
from station_backtage.base.base_mysql import DBUtil

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mysql_data  = DBUtil( "wt_bigdata")

    def setup(self):
        time.sleep(0.1)

    @classmethod
    def teardown_class(cls):
        time.sleep(2)

    @parameterized.expand(read_excel("test_data.xlsx", "piaowu"))
    def test( self, ele, event_type, event_type_3):
        n = 0
        m = 0
        if event_type == "1":
            args = str(ele)
            sql1 = 'select element_id, event_type from buried_point where app_id=12 and element_id="{}"'.format(args)
            rows = self.mysql_data.get_sql(sql1)
            try :
                print(rows)
                for row in rows:
                    if row[1] == 1:
                        n = row[1]
                assert str(rows[0][0]) == args and n == 1
            except IndexError :
                assert 0==1
        if event_type == "2":
            args = str(ele)
            print(args)
            sql1 = 'select page_name,event_type from buried_point where app_id=12 and page_name="{}"'.format(args)
            rows = self.mysql_data.get_sql(sql1)
            time.sleep(1)
            try:
                print(rows)
                for row in rows:
                    if row[1] == 2:
                        n = row[1]
                    if row[1] == 3:
                        m = row[1]
                assert str(rows[0][0]) == args and n == 2 and m == 3
            except IndexError:
                assert 0 == 1

    def teardown(self):
        pass



if __name__ == '__main__':
    unittest.main()
