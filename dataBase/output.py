#随机数生成器
import random
from LinkToSQLSever.link import linkSqlite
from LinkToSQLSever.Add import Add
import sqlite3

#生成随机整数
flag = 1
if __name__== "__main__":
    """
    # 创建一个访问数据库test.db的连接
    # 服务器名，账户，密码，数据库名
    connect = pymssql.connect('(localhost)', 'sa', '123456', '智能体育考核系统new')
    if connect:
        print("Connected Successfully!")
    cursor = connect.cursor()
    """
    conn = sqlite3.connect("test.db")
    """
    try:
        conn = sqlite3.connect("test.db")
    except sqlite3.Error as e:
        print "connection db failed","\n",e.args[0]
        return"""
    # 创建游标对象
    cursor = conn.cursor()
    linkSqlite(cursor)
    i = 0
    while flag ==1:
        stu_id = random.randint(0,100)
        type = "situp"
        num = random.randint(0,100)
        mark = random.choice([0,1])
        #time = random.random()
        #time = random.choice([1,2,0.0])
        time = random.randint(0,60)
        #reason = 'waist angle is nostandard'
        waist_angle = random.choice([0, 1])
        arm_position = random.choice([0, 1])
        elbow_angle = random.choice([0, 1])
        chin_height = random.choice([0, 1])
        flag = 1
        #if time != 0.0:
        if i != 3:
            # 调用数据库操作方法
            Add(cursor,flag, stu_id, type, mark, num, time, waist_angle, arm_position, elbow_angle, chin_height)
            conn.commit()
        else:
            break
        i = i + 1
    conn.close()