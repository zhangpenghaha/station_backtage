# 使用自定义的 pymysql 工具类
from tkinter import *
import pymysql
import string

from station_backtage.base.base_analyze import  mysql_file


class DBUtil():

    def __init__( self, mysql_datas):
        self.mysql_data = mysql_datas

    # 封装获取连接的函数
    # 返回值 connection
    # 参数不设置，后期从配置文件读取
    # @classmethod
    def get_conn(self):
        self.mysqls = self.mysql_data
        config_mysql = mysql_file("mysql.yaml",self.mysqls)
        host = str(config_mysql["host"])
        port = int(config_mysql["port"])
        database = str(config_mysql["database"])
        user = str(config_mysql["user"])
        password = str(config_mysql["password"])
        charset = config_mysql["charset"]
        conn = pymysql.connect(host = host, port=port, database=database, user=user,password=password,charset=charset)
        return conn

    # 封装获取游标对象的函数
    # 参数： 连接对象
    # 返回值： 游标对象
    @classmethod
    def get_cursor(cls,conn):
        cursor = conn.cursor()
        return cursor

    # 封装资源释放的函数
    # 参数： cursor / conn
    # 返回值： 无
    @classmethod
    def close_res(cls,cursor,conn):
        if cursor:
            cursor.close()
            cursor = None

        if conn:
            conn.close()
            conn = None

    def get_sql(self, sql):
        # 获取连接

        conn = self.get_conn()
        # 获取游标
        cursor = self.get_cursor(conn)
        # 核心： SQL语句,并打印所有

        sql1 =sql
        cursor.execute(sql1)
        conn.commit()
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        # 释放资源
        self.close_res(cursor,conn)
        return rows
if __name__ == '__main__':
    DBUtil("wt_bigdata").get_conn()