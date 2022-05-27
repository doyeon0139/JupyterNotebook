import sys       
import PyQt5
from PyQt5.QtGui import *   
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
from PyQt5 import uic  

CalUI = 'C:/pyqt/ui/calculator2.ui'   

class MainDialog(QDialog):   
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)   

        self.num_pushButton_1.clicked.connect(lambda state, button=self.num_pushButton_1 : self.NumClicked(state, button))  
        self.num_pushButton_2.clicked.connect(lambda state, button=self.num_pushButton_2 : self.NumClicked(state, button))  

   

    def NumClicked(self, state, button):   # 연동시킬 함수를 만들어 볼까요?
        exist_line_text = self.q_lineEdit.text()  
        now_num_text = button.text()
        self.q_lineEdit.setText(exist_line_text + now_num_text)


app = QApplication(sys.argv)  

main_dialog = MainDialog()
main_dialog.show()
app.exec_()

