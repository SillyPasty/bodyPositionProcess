import sys
from PySide2.QtCore import Qt,QTimer
from PySide2.QtWidgets import QApplication, QWidget, QComboBox,QPushButton ,QLabel,QVBoxLayout,QMainWindow,QLineEdit,QLCDNumber
                              
from PySide2.QtCore import Slot

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300,300)

        
        #输入个人信息
        label1=QLabel("请输入姓名")
        name=QLineEdit()
        
        #文本标签
        label2=QLabel("请选择测试项目")
        label2.resize(20,20)
        
        #下拉选择框
        cb=QComboBox(self)
        cb.move(100,50)
        cb.addItem('仰卧起坐')
        cb.addItem('俯卧撑')
        cb.addItem('引体向上')


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
        layout.addWidget(name)
        layout.addWidget(label2)
        layout.addWidget(cb)
        layout.addWidget(button1)
        layout.addWidget(self.clock)
        self.setLayout(layout)

    def start(self):
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)

    def updateTime(self):
        if self.a >= 0:
            self.a -= 1
        self.clock.display(self.a)
    
       

if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
