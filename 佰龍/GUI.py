import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import time





class MainWidget(QWidget):
  def __init__(self, parent=None):
    super(MainWidget, self).__init__(parent)
    
    self._width = 800
    self._height = 600
    self.setFixedSize(self._width, self._height)
    #设置标题
    self.setWindowTitle('QThread多現程例子')

    #实例化多线程对象
    self.thread = Worker()

    #实例化列表控件与按钮控件
    self.listFile = QListWidget()


   # self.btnStart = QPushButton('开始')

    # 把控件放置在栅格布局中
    # layout = QGridLayout(self)
    # layout.addWidget(self.listFile, 0, 0, 1, 2)
   # layout.addWidget(self.btnStart, 1, 1)
    
    formLayout = QFormLayout()
    groupBox = QGroupBox()
        
    # with open("log.json","r",encoding="utf-8") as f:  
     
    #             for row in f.readlines():
                   
    #                 label2 = QLabel(row)
                   
    #                 formLayout.addRow( label2)
       
    groupBox.setLayout(formLayout)

    scroll = QScrollArea()
    scroll.setWidget(groupBox)
    scroll.setWidgetResizable(True)

    layout = QVBoxLayout(self)
    layout.addWidget(scroll)
    layout.addWidget(self.listFile)
    
    
    
    #信号与槽函数的连接
    #self.btnStart.clicked.connect(self.slotStart)
    self.thread.start()
    self.thread.sinOut.connect(self.slotAdd)
    
  def slotAdd(self, file_inf):
    #向列表控件中添加条目

    self.listFile.addItem(file_inf)
    

  #def slotStart(self):
    #开始按钮不可点击，线程开始
    #self.btnStart.setEnabled(False)
    self.thread.start()
    


class Worker(QThread):
  sinOut = pyqtSignal(str)

  def __init__(self, parent=None):
    super(Worker, self).__init__(parent)
    #设置工作状态与初始num数值
    self.working = True
    self.num = 0

  def __del__(self):
    #线程状态改变与线程终止
    self.working = False
    self.wait()

  def run(self):
      if self.working == True:
      #获取文本
        with open("log.json","r",encoding="utf-8") as f:  
            data = f.read()
        self.sinOut.emit(data)
        self.sleep(10)


if __name__ == '__main__':
     

    while True:
        app = QApplication(sys.argv)
        demo = MainWidget()
        demo.show()
        sys.exit(app.exec_())
