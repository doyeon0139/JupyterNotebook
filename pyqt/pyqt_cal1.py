# -*- coding: utf-8 -*-



import sys       
import PyQt5
from PyQt5.QtGui import *   
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * #  from PyQt5.QtGui import * 은 PyQt5 폴더의 QtGui 파일에서 모든 클래스와 함수를 불러오겠다는 의미

class MainDialog(QDialog):   
    def __init__(self):
        QDialog.__init__(self, None)   
            
app = QApplication(sys.argv)  
print(sys.argv)  # 파일의 절대경로
main_dialog = MainDialog()
main_dialog.show()  
app.exec_()  
