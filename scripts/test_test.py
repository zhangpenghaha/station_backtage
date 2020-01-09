# 使用自定义的 pymysql 工具类
import time
import unittest


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setup(self):
        time.sleep(0.1)

    @classmethod
    def teardown_class(cls):
        time.sleep(2)


    def test( self):
        print(1)




