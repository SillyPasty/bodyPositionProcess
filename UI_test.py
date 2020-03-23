import sys
from PySide2.QtCore import Qt,QTimer
from PySide2.QtWidgets import QApplication, QWidget, QComboBox,QPushButton ,QLabel,QVBoxLayout,QMainWindow,QLineEdit,QLCDNumber
from datetime import datetime, timedelta
                              
from PySide2.QtCore import Slot, Signal
import PySide2.QtCore as QtCore

class Demo(QWidget, QtCore.QObject):
    s_start_analysis = Signal(str, int)
    def __init__(self):
        super().__init__()
        self.resize(300,300)
        
        #输入个人信息
        label1=QLabel("请输入姓名")
        self.name=QLineEdit()
        
        
        #文本标签
        label2=QLabel("请选择测试项目")
        label2.resize(20,20)
        
        #下拉选择框
        self.cb=QComboBox(self)
        self.cb.move(100,50)
        self.cb.addItem('仰卧起坐')
        self.cb.addItem('俯卧撑')
        self.cb.addItem('引体向上')


        #开始 结束测试按钮
        button1 = QPushButton("开始测试")
        button1.clicked.connect(self.start)

        #倒计时功能
        self.a = 60
        self.clock=QLCDNumber()
        self.clock.display(self.a)
        
        #布局
        layout =QVBoxLayout(self)
        layout.addWidget(label1)
        layout.addWidget(self.name)
        layout.addWidget(label2)
        layout.addWidget(self.cb)
        layout.addWidget(button1)
        layout.addWidget(self.clock)
        self.setLayout(layout)
        # 新建线程
        self.newThread = QtCore.QThread()
        self.task = Task()


    def start(self):
        types = self.cb.currentText()
        self.task.moveToThread(self.newThread)
        # 连接信号
        self.task.s_update_time.connect(self.updateTime)
        self.s_start_analysis.connect(self.task.task)
        # 开始线程
        self.newThread.start()
        # 开始任务
        self.s_start_analysis.emit(types, 60)


    def updateTime(self, sec):
        self.clock.display(sec)
    

class Task(QtCore.QObject):
    s_update_time = Signal(int)
    def __init__(self):
        super().__init__()  
    
    def task(self, type, length):
        print(type)
        startTime = datetime.now()
        leng = 0
        while leng < length:
            curTime = datetime.now()
            delta = curTime - startTime
            if delta.seconds != leng:
                leng = delta.seconds
                self.s_update_time.emit(length - leng)

        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())