

def linkSqlite(cursor):
    sql_del = "DROP TABLE IF EXISTS stu;"
    cursor.execute(sql_del)
    # 创建一个user表
    cursor.execute(
        "CREATE TABLE stu(Flag INTEGER,Stu_id INTEGER,"
        "Type TEXT, Num INTEGER, Mark INTEGER, Time REAL,"
        "Waist_angle INTERGER, Arm_position INTEGER,"
        "Elbow_angle INTEGER, Chin_height INTEGER)")
    # Add(cursor,flag, stu_id, type, mark, num, time, reason)