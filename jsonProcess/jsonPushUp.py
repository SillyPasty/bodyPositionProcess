from jsonProcess.TJsonProcess import TJsonProcess
# import PySide2.QtCore as QtCore
from datetime import datetime
import cv2

class JsonPushUp(TJsonProcess):

    def __init__(self, folder_path):
        super().__init__(folder_path)

    def process(self, types, period):
        print(types)
        startTime = datetime.now()
        length = 0
        vStream = cv2.VideoCapture(0)
        while length < period:
            _, frame = vStream.read()
            cv2.imshow('ex1', frame)
            curTime = datetime.now()
            delta = curTime - startTime
            if delta.seconds != length:
                length = delta.seconds
                # self.hisInfo.add(id=length, flag=1, stuno=1, type='situp', mark=1,
                #                 num=1, time=datetime.now(), waist=1, arm=1,
                #                 elbow=1, chin=1, flag2=0)
                self.signal_update_time.emit(period - length)

            if cv2.waitKey(1) == ord('q'):
                break
