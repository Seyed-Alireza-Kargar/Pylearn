# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GuessNumber.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(510, 250)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.txt_input = QLineEdit(self.centralwidget)
        self.txt_input.setObjectName(u"txt_input")
        self.txt_input.setGeometry(QRect(90, 50, 113, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 10, 271, 20))
        self.label.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.btn_Check = QPushButton(self.centralwidget)
        self.btn_Check.setObjectName(u"btn_Check")
        self.btn_Check.setGeometry(QRect(210, 50, 111, 31))
        self.btn_Check.setStyleSheet(u"background-color: #9333a7; border-radius: 16px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 140, 271, 20))
        self.label_2.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.lbl_remain = QLabel(self.centralwidget)
        self.lbl_remain.setObjectName(u"lbl_remain")
        self.lbl_remain.setGeometry(QRect(250, 140, 271, 20))
        self.lbl_remain.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 85, 255);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 110, 51, 20))
        self.label_4.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.lbl_help = QLabel(self.centralwidget)
        self.lbl_help.setObjectName(u"lbl_help")
        self.lbl_help.setGeometry(QRect(70, 110, 351, 20))
        self.lbl_help.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Guess Number", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Input a number between 0 and 100:", None))
        self.btn_Check.setText(QCoreApplication.translate("MainWindow", u"Guess", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"The remain number of guess:", None))
        self.lbl_remain.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Help:", None))
        self.lbl_help.setText("")
    # retranslateUi

