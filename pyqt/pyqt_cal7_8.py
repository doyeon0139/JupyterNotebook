import sys       
import PyQt5
from PyQt5.QtGui import *   
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
from PyQt5 import uic  

CalUI = 'C:/pyqt/ui/calculator3.ui'   

class MainDialog(QDialog):   
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)   

        self.num_pushButton_1.clicked.connect(lambda state, button=self.num_pushButton_1 : self.NumClicked(state, button))  
        self.num_pushButton_2.clicked.connect(lambda state, button=self.num_pushButton_2 : self.NumClicked(state, button))  
        self.num_pushButton_3.clicked.connect(lambda state, button=self.num_pushButton_3 : self.NumClicked(state, button))  
        self.num_pushButton_4.clicked.connect(lambda state, button=self.num_pushButton_4 : self.NumClicked(state, button))  
        self.num_pushButton_5.clicked.connect(lambda state, button=self.num_pushButton_5 : self.NumClicked(state, button))  
        self.num_pushButton_6.clicked.connect(lambda state, button=self.num_pushButton_6 : self.NumClicked(state, button))  
        self.num_pushButton_7.clicked.connect(lambda state, button=self.num_pushButton_7 : self.NumClicked(state, button))  
        self.num_pushButton_8.clicked.connect(lambda state, button=self.num_pushButton_8 : self.NumClicked(state, button))  
        self.num_pushButton_9.clicked.connect(lambda state, button=self.num_pushButton_9 : self.NumClicked(state, button))  
        self.num_pushButton_0.clicked.connect(lambda state, button=self.num_pushButton_0 : self.NumClicked(state, button)) 

        self.sign_pushButton_1.clicked.connect(lambda state, button=self.sign_pushButton_1 : self.NumClicked(state, button))  
        self.sign_pushButton_2.clicked.connect(lambda state, button=self.sign_pushButton_2 : self.NumClicked(state, button))  
        self.sign_pushButton_3.clicked.connect(lambda state, button=self.sign_pushButton_3 : self.NumClicked(state, button))  
        self.sign_pushButton_4.clicked.connect(lambda state, button=self.sign_pushButton_4 : self.NumClicked(state, button))  

        self.result_pushButton.clicked.connect(self.MakeResult)  
        self.reset_pushButton.clicked.connect(self.Reset)  
        self.del_pushButton.clicked.connect(self.Delete)  

    def NumClicked(self, state, button):   # 연동시킬 함수를 만들어 볼까요?
        exist_line_text = self.q_lineEdit.text()  
        now_num_text = button.text()
        self.q_lineEdit.setText(exist_line_text + now_num_text)

    def MakeResult(self):
        try:
            result = eval(self.q_lineEdit.text())
            self.a_lineEdit.setText(str(result))  # str로 문자열로 형변환을 해주어야
        except Exception as e:
            print(e)
            # pass


    def Reset(self):                  # reset 버튼은 계산기에서 C가 적혀있는 버튼으로, 계산기의 모든 숫자를 초기화하는 역할
        self.q_lineEdit.clear()       # q_lineedit은 지우고
        self.a_lineEdit.setText('0')  # a_lineedit은 문자열 0을 입력

    def Delete(self):               
        exist_line_text = self.q_lineEdit.text()
        exist_line_text = exist_line_text[:-1]
        self.q_lineEdit.setText(exist_line_text)


app = QApplication(sys.argv)  

main_dialog = MainDialog()
main_dialog.show()
app.exec_()

