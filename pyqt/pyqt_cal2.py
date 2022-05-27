import sys       
import PyQt5
from PyQt5.QtWidgets import  QApplication
from PyQt5.QtGui import *   
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 

class MainDialog(QDialog):  
    def __init__(self):
        QDialog.__init__(self, None)
        self.setFixedSize(300, 200)  
        self.lineEdit = QLineEdit(self) 
        self.pushButton = QPushButton(self)  
        self.pushButton.move(0, 100) 

app = QApplication(sys.argv)  

main_dialog = MainDialog()
main_dialog.show()
app.exec_()

"""

"""