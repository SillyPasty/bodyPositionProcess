import sys
from PySide2.QtWidgets import QWidget, QComboBox,QPushButton ,QLabel,QVBoxLayout,QMainWindow,QLineEdit,QLCDNumber
import PySide2.QtCore as QtCore

class TLoginWindow(QWidget, QtCore.QObject):
    def __init__(self):
        super().__init__()

        self.resize(300,300)
        
        #输入个人信息
        label_name=QLabel("请输入姓名")
        self.edit_name=QLineEdit()
        
        #文本标签
        label_pos=QLabel("请选择测试项目")
        label_pos.resize(20,20)
        
        #下拉选择框
        self.cbox_pos=QComboBox(self)
        self.cbox_pos.move(100,50)
        self.cbox_pos.addItem('仰卧起坐')
        self.cbox_pos.addItem('俯卧撑')
        self.cbox_pos.addItem('引体向上')

        #开始测试按钮
        self.start_button = QPushButton("开始测试")
        # button1.clicked.connect(self.start)

        #倒计时功能
        init = 60
        self.lcd_cntDown=QLCDNumber()
        self.lcd_cntDown.display(init)
        
        #布局
        layout =QVBoxLayout(self)
        layout.addWidget(label_name)
        layout.addWidget(self.edit_name)
        layout.addWidget(label_pos)
        layout.addWidget(self.cbox_pos)
        layout.addWidget(self.start_button)
        layout.addWidget(self.lcd_cntDown)
        self.setLayout(layout)
