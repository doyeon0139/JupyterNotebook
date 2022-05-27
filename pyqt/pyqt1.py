import sys
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

print(sys.argv)

CalUI = 'D:/python/a_pyqt/ui/fc_main.ui'

class MainDialog(QDialog):   # QDialog를 상속하는 class
    def __init__(self):
        QDialog.__init__(self, None, Qt.WindowStaysOnTopHint)
        uic.loadUi(CalUI, self)

        self.num_pushButton_1.clicked.connect(lambda state, button = self.num_pushButton_1 : self.NumClicked(state, button))
        self.num_pushButton_2.clicked.connect(lambda state, button = self.num_pushButton_2 : self.NumClicked(state, button))
        self.num_pushButton_3.clicked.connect(lambda state, button = self.num_pushButton_3 : self.NumClicked(state, button))
        self.num_pushButton_4.clicked.connect(lambda state, button = self.num_pushButton_4 : self.NumClicked(state, button))
        self.num_pushButton_5.clicked.connect(lambda state, button = self.num_pushButton_5 : self.NumClicked(state, button))
        self.num_pushButton_6.clicked.connect(lambda state, button = self.num_pushButton_6 : self.NumClicked(state, button))
        self.num_pushButton_7.clicked.connect(lambda state, button = self.num_pushButton_7 : self.NumClicked(state, button))
        self.num_pushButton_8.clicked.connect(lambda state, button = self.num_pushButton_8 : self.NumClicked(state, button))
        self.num_pushButton_9.clicked.connect(lambda state, button = self.num_pushButton_9 : self.NumClicked(state, button))
        self.num_pushButton_0.clicked.connect(lambda state, button = self.num_pushButton_0 : self.NumClicked(state, button))

        self.sign_pushButton_1.clicked.connect(lambda state, button = self.sign_pushButton_1 : self.NumClicked(state, button))
        self.sign_pushButton_2.clicked.connect(lambda state, button = self.sign_pushButton_2 : self.NumClicked(state, button))
        self.sign_pushButton_3.clicked.connect(lambda state, button = self.sign_pushButton_3 : self.NumClicked(state, button))
        self.sign_pushButton_4.clicked.connect(lambda state, button = self.sign_pushButton_4 : self.NumClicked(state, button))

        self.p_open_pushButton.clicked.connect(lambda state, button = self.p_open_pushButton : self.NumClicked(state, button))
        self.p_close_pushButton.clicked.connect(lambda state, button = self.p_close_pushButton : self.NumClicked(state, button))
        self.dot_pushButton.clicked.connect(lambda state, button = self.dot_pushButton : self.NumClicked(state, button))
        self.per_pushButton.clicked.connect(lambda state, button = self.per_pushButton : self.NumClicked(state, button))

        
        self.result_pushButton.clicked.connect(self.MakeResult)
        self.reset_pushButton.clicked.connect(self.Reset)
        self.del_pushButton.clicked.connect(self.Delete)
       

       

    def NumClicked(self,state, button):

        if button == self.per_pushButton:
            now_num_text = '*0.01'

        else:
            now_num_text = button.text()

        exit_line_text = self.q_lineEdit.text()
        self.q_lineEdit.setText(exit_line_text + now_num_text)

    def MakeResult(self):

        try:
            result = eval(self.q_lineEdit.text())

            self.answer_lineEdit.setText(str(result))
            self.answer_textBrowser.setText(str(result))
            # self.setFixedSize(300, 200)

        except Exception as e:
            print(e)
# self.lineEdit = QLineEdit(self)
# self.pushButton= QPushButton(self)
# self.pushButton.move(0, 100)

    def Reset(self):
        self.q_lineEdit.clear()
        self.answer_lineEdit.setText('0')
        self.answer_textBrowser.setText('0')

    def Delete(self):
        exist_line_text = self.q_lineEdit.text()
        exist_line_text = exist_line_text[:-1]
        self.q_lineEdit.setText(exist_line_text)

    

app = QApplication(sys.argv)    # app은 QApplication() 클래스를 상속받는 객체, QApplication()은 프로그램을 실행시키는 메소드
main_dialog = MainDialog()      # MainDailog 를래스를 상속받는 객체
main_dialog.show()              # show()는 화면에 띄우는 메소드
app.exec_()                     # exec_() 메소드는 프로그램을 이벤트루프로 진입시키는 메소드
                                # 이벤트루프 - 프로그램을 무한루프에서 계속 실행시키고, 프로그램의 이벤트를 받아서 처리..

                            
