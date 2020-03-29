import random
import pymssql


class HisInfoDb():

    def __init__(self):
        self.hisDb = pymssql.connect('127.0.0.1:1433', 'admin', '123456', 'AIPE', charset='utf8')
        if self.hisDb:
            print("Connected Successfully!")
        self.cursor = self.hisDb.cursor()


    def __del__(self):
        self.hisDb.close()


    def add(self, id, flag, stuno, type, mark,
            num, time, waist, arm,
            elbow, chin, flag2):
        if flag == 1:
            try:
                sql = "INSERT INTO Queue(id, flag, stuno, type, num, \
                        mark, time, waist, arm, elbow, \
                        chin, flag2) VALUES (%d,%d,%d,%s,%d,%d,%s,%d,%d,%d,%d,%d)"
                para = (id, flag, stuno, type, num, mark, time,
                        waist, arm, elbow, chin, flag2)
                print(1)
                self.cursor.execute(sql, para)
                print(2)
                self.hisDb.commit()
                print('success')
            except Exception as e:
                print(e)
