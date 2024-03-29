import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.buttons = [[self.ui.btn1, self.ui.btn2, self.ui.btn3, self.ui.btn4],
                        [self.ui.btn5, self.ui.btn6, self.ui.btn7, self.ui.btn8],
                        [self.ui.btn9, self.ui.btn10, self.ui.btn11, self.ui.btn12],
                        [self.ui.btn13, self.ui.btn14, self.ui.btn15, self.ui.btn16]]


        check_solvable = False
        while not check_solvable:

            r = []
            while len(r) < 16:
                m = random.randint(1, 16)
                if not m in r:
                    r.append(m)
                inv_count = 0
                
            for i in range(16):
                for j in range(i + 1,16):
                    if (r[j] != 16 and r[i] != 16 and r[i] > r[j]):
                        inv_count+=1

                if r[i] == 16:
                    posX = 4 - i//4

            if (inv_count + posX) & 1:
                check_solvable = True
            else:
                check_solvable = False

        for i in range(4):
            for j in range(4):
                self.buttons[i][j].setText(str(r[4*i+j]))
                self.buttons[i][j].clicked.connect(partial(self.play, i, j))
                if r[4*i+j] == 16:
                    self.buttons[i][j].setVisible(False)
                    self.empty_i = i
                    self.empty_j = j

    def play(self, i ,j):
        if abs(i-self.empty_i) + abs(j-self.empty_j) == 1:

            self.buttons[self.empty_i][self.empty_j].setText(self.buttons[i][j].text())
            self.buttons[i][j].setText('16')

            self.buttons[self.empty_i][self.empty_j].setVisible(True)
            self.buttons[i][j].setVisible(False)

            self.empty_i = i
            self.empty_j = j

            if self.check_win():
                msg_box = QMessageBox()
                msg_box.setText('YOU ARE WINNNN 🎊🎊🎉')
                msg_box.exec()

    def check_win(self):
        index = 1
        for i in range(4):
            for j in range(4):
                if int(self.buttons[i][j].text()) != index:
                    return False
                index += 1
        return True

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()

app.exec()