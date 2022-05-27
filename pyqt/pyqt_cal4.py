import sys       
import PyQt5
from PyQt5.QtGui import *   
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
from PyQt5 import uic  

CalUI = 'C:/pyqt/ui/calculator1.ui'   

class MainDialog(QDialog):   
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)   

        self.num_pushButton_1.clicked.connect(self.NumClicked)  
        
    def NumClicked(self):   
        print('나 클릭됐다~') 
        print(self.num_pushButton_1.text()) 
        
        exist_line_text = self.q_lineEdit.text()  # 

        now_num_text = self.num_pushButton_1.text()
        self.q_lineEdit.setText(exist_line_text + now_num_text)


app = QApplication(sys.argv)  

main_dialog = MainDialog()
main_dialog.show()
app.exec_()

