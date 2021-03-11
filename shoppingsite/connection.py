from pymysql import *

class connections:
    conn = connect(
        host='localhost',
        user='root',
        password='',
        database='shopping',
        # cursorclass=cursors.DictCursor
    )