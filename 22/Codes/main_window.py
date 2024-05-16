# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.task_table = QTableWidget(self.centralwidget)
        if (self.task_table.columnCount() < 7):
            self.task_table.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.task_table.setObjectName(u"task_table")
        self.task_table.setGeometry(QRect(10, 10, 780, 400))
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(10, 420, 200, 20))
        self.title_input = QLineEdit(self.centralwidget)
        self.title_input.setObjectName(u"title_input")
        self.title_input.setGeometry(QRect(10, 440, 200, 30))
        self.label_description = QLabel(self.centralwidget)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(220, 420, 200, 20))
        self.description_input = QLineEdit(self.centralwidget)
        self.description_input.setObjectName(u"description_input")
        self.description_input.setGeometry(QRect(220, 440, 200, 30))
        self.label_time = QLabel(self.centralwidget)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setGeometry(QRect(430, 420, 150, 20))
        self.time_input = QDateTimeEdit(self.centralwidget)
        self.time_input.setObjectName(u"time_input")
        self.time_input.setGeometry(QRect(430, 440, 150, 30))
        self.label_priority = QLabel(self.centralwidget)
        self.label_priority.setObjectName(u"label_priority")
        self.label_priority.setGeometry(QRect(590, 420, 100, 20))
        self.priority_input = QComboBox(self.centralwidget)
        self.priority_input.addItem("")
        self.priority_input.addItem("")
        self.priority_input.setObjectName(u"priority_input")
        self.priority_input.setGeometry(QRect(590, 440, 100, 30))
        self.add_task_button = QPushButton(self.centralwidget)
        self.add_task_button.setObjectName(u"add_task_button")
        self.add_task_button.setGeometry(QRect(700, 440, 100, 30))
        self.sort_tasks_button = QPushButton(self.centralwidget)
        self.sort_tasks_button.setObjectName(u"sort_tasks_button")
        self.sort_tasks_button.setGeometry(QRect(700, 480, 100, 30))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.task_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.task_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem2 = self.task_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem3 = self.task_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem4 = self.task_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Priority", None));
        ___qtablewidgetitem5 = self.task_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Done", None));
        ___qtablewidgetitem6 = self.task_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.title_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.label_description.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.description_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_priority.setText(QCoreApplication.translate("MainWindow", u"Priority", None))
        self.priority_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.priority_input.setItemText(1, QCoreApplication.translate("MainWindow", u"High", None))

        self.add_task_button.setText(QCoreApplication.translate("MainWindow", u"Add Task", None))
        self.sort_tasks_button.setText(QCoreApplication.translate("MainWindow", u"Sort Tasks", None))
    # retranslateUi

