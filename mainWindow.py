from ui.loginWinTemplate import TLoginWindow
from PySide2.QtWidgets import QApplication
from jsonProcess.jsonPushUp import JsonPushUp
import PySide2.QtCore as QtCore
import sys

class MainWindow(TLoginWindow):
    # 初始化线程与信号
    newThread = QtCore.QThread()
    signal_start_process = QtCore.Signal(str, int)

    def __init__(self):
        super().__init__()
        self.start_button.clicked.connect(self.start)

    # SLOT 更新倒计时
    def updateTime(self, sec):
        self.lcd_cntDown.display(sec)


    def start(self):
        types = self.cbox_pos.currentText()
        path = r'D:\Programme\Python\IntelligentPEExam'
        self.process_task = JsonPushUp(path)
        self.process_task.moveToThread(self.newThread)
        # 连接信号
        self.process_task.signal_update_time.connect(self.updateTime)
        self.signal_start_process.connect(self.process_task.process)
        # 开始线程
        self.newThread.start()
        # 开始任务
        self.signal_start_process.emit(types, 60)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())