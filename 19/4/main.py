import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication,QMainWindow,QMessageBox
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

Guess_Cnt=1
Computer_Num=random.randint(1,100)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_Check.clicked.connect(self.check)


    def check(self):
        global Guess_Cnt
        if(int(self.ui.lbl_remain.text())==0):
                msgBox=QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Information)
                msgBox.setText("You lose!!!. The correct Number is "+str(Computer_Num))
                self.ui.lbl_help.setText("You lose!!!. The correct Number is "+str(Computer_Num))
                msgBox.exec()
                return

        User_Num=int(self.ui.txt_input.text())
        if(Computer_Num==User_Num):
            if(Guess_Cnt==1):
                msgBox=QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Information)
                msgBox.setText("You Win in your first guess 🥳✨")
                self.ui.lbl_help.setText("You Win in your first guess 🥳✨")
                msgBox.exec()
            else:
                msgBox=QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Information)
                msgBox.setText("✨You Win after "+str(Guess_Cnt)+ " times✨")
                self.ui.lbl_help.setText("✨You Win after "+str(Guess_Cnt)+ " times✨")
                msgBox.exec()
            return
        if(User_Num<Computer_Num):
                msgBox=QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Information)
                msgBox.setText("Your guess is lower. The remain guess chances is "+ str(10-Guess_Cnt))
                self.ui.lbl_help.setText("Guess a greater number ⬆.")
                msgBox.exec()      
        else:
                msgBox=QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Information)
                msgBox.setText("Your guess is greater.The remain guess chances is "+str(10-Guess_Cnt))
                self.ui.lbl_help.setText("Guess a lower number ⬇")
                msgBox.exec()
        
        self.ui.lbl_remain.setText(str(10-Guess_Cnt))
        Guess_Cnt+=1





my_app=QApplication(sys.argv)
My_Window=MainWindow()
My_Window.show()
my_app.exec()