

def Add(cursor, id, flag, stuno, type, mark,
        num, time, waist, arm,
        elbow, chin, flag2):
    while flag == 1:
        sql = "INSERT INTO Queue(id, flag, stuno, type, num, \
            mark, time, waist, arm, elbow, \
            chin, flag2) VALUES (%d,%d,%d,%s,%d,%d,%s,%d,%d,%d,%d,%d)"
        para = (id, flag, stuno, type, num, mark, time,
                waist, arm, elbow, chin, flag2)
        cursor.execute(sql, para)
        break