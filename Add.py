def Add (cursor, flag, stu_id, type, mark, num, time, waist_angle, arm_position, elbow_angle, chin_height):
    while flag == 1:
        sql = "INSERT INTO stu(Flag, Stu_id, Type, Num, Mark, Time, Waist_angle, Arm_position, Elbow_angle, Chin_height) VALUES (?,?,?,?,?,?,?,?,?,?)"
        para = (flag,stu_id,type,num,mark,time,waist_angle, arm_position, elbow_angle, chin_height)
        cursor.execute(sql,para)
        break