from LinkToSQLSever.Add import Add

def linkSqlite(cursor):
    """
    实现功能：在录入某个人或某段考试数据时在数据库中创建表并录入，每当flag为1时向表中写入数据
    """
    sql_del = "DROP TABLE IF EXISTS stu;"
    cursor.execute(sql_del)
    #创建一个user表
    cursor.execute("CREATE TABLE stu(Flag INTEGER,Stu_id INTEGER,Type TEXT,Num INTEGER,Mark INTEGER,Time REAL,Waist_angle INTERGER, Arm_position INTEGER, Elbow_angle INTEGER, Chin_height INTEGER)")


"""
import pymssql
def linkSqlite(cursor):
    #实现功能：在录入某个人或某段考试数据时在数据库中创建表并录入，每当flag为1时向表中写入数据
    #创建游标对象
    cursor = connect.cursor()
    sql_del = "DROP TABLE IF EXISTS stu;"
    cursor.execute(sql_del)
    #创建一个user表
    '''
    CREATE TABLE Stu
    {
        Stu_id int PRIMARY KEY,#据情况可改为varchar(10），10指的是字符串长度
        Type varchar(8) NULL,
        Num int NULL,
        Mark int NULL CHECK(mark in (1,0)),
        Time double NULL,
        Reason varchar(25) NULL,
    }
    '''
    cursor.execute("CREATE TABLE stu(Stu_id int,Type varchar(8),Num int,Mark int,Time double,Waist_angle int, Arm_position int, Elbow_angle int, Chin_height int)")
"""
#一班 王一 甲乙丙 123
#二班 丁二  丁戊 5
