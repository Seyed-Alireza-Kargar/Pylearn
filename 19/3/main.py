import sys
import random
import secrets
import string
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        self.setFixedSize(479,409)
        self.letters = string.ascii_lowercase
        self.upper = string.ascii_uppercase
        self.digits = string.digits
        self.special = string.punctuation
        self.stlvl = self.letters + self.upper
        self.mdlvl = self.letters + self.upper + self.digits
        self.hrlvl = self.letters + self.upper + self.digits + self.special
        self.password = ""
        self.ui.btngen1.clicked.connect(self.generate_lv1)
        self.ui.btngen2.clicked.connect(self.generate_lv2)
        self.ui.btngen3.clicked.connect(self.generate_lv3)

    def generate_lv1(self):
        for i in range(8):
            self.password += "".join(secrets.choice(self.stlvl))
        self.ui.line_edit1.setText(str(self.password))
        self.password = ""
        
        

    def generate_lv2(self):
        range1 = random.randint(10, 15)
        for i in range(range1):
            self.password += "".join(secrets.choice(self.mdlvl))
        self.ui.line_edit2.setText(str(self.password))
        self.password = ""

    def generate_lv3(self):
        range2 = random.randint(14, 20)
        for i in range(range2):
            self.password += "".join(secrets.choice(self.hrlvl))
        self.ui.line_edit3.setText(str(self.password))
        self.password = ""


app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()