from jsonProcess.TJsonProcess import TJsonProcess
# import PySide2.QtCore as QtCore
from datetime import datetime

class JsonPushUp(TJsonProcess):

    def __init__(self, folder_path):
        super().__init__(folder_path)

    def process(self, types, period):
        print(types)
        startTime = datetime.now()
        length = 0
        while length < period:
            curTime = datetime.now()
            delta = curTime - startTime
            if delta.seconds != length:
                length = delta.seconds
                self.signal_update_time.emit(period - length)



        
