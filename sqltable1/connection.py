from pymysql import *


class connections:
    conn = connect(host='localhost',
        user='root',
        password='',
        database='test')