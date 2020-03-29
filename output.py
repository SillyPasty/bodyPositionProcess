# 随机数生成器
import random
from linkToSQLServer.Add import Add
import pymssql
import datetime

# 生成随机整数
flag = 1
if __name__ == "__main__":
    # 服务器名，账户，密码，数据库名
    conn = pymssql.connect('127.0.1.1:1433', 'sa', '123456', '改成自己数据库的名字', charset='utf8')
    if conn:
        print("Connected Successfully!")
    cursor = conn.cursor()
    # 创建游标对象
    i = 0
    while flag == 1:
        stuno = random.randint(0, 100)
        type = "situp"
        num = random.randint(0, 100)
        mark = random.choice([0, 1])
        # time = random.random()
        # time = random.choice([1,2,0.0])
        time = datetime.datetime.now()
        # reason = 'waist angle is nostandard'
        waist = random.choice([0, 1])
        arm = random.choice([0, 1])
        elbow = random.choice([0, 1])
        chin = random.choice([0, 1])
        flag = 1
        flag2 = 0
        id = i+1
        if i != 3:
            # 调用数据库操作方法
            Add(cursor, id, flag, stuno, type,
                mark, num, time, waist, arm, elbow,
                chin, flag2)
            conn.commit()
        else:
            break
        i = i + 1
    conn.close()
