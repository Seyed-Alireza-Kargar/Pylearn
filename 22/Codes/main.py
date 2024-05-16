import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QPushButton, QHBoxLayout, QWidget
from PySide6.QtCore import Qt, QDate, QSignalMapper
from main_window import Ui_MainWindow
from database import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.time_input.setMinimumDate(QDate.currentDate())
        self.ui.task_table.setColumnHidden(0, True)
        self.ui.task_table.setColumnWidth(6, 150)
        self.ui.task_table.setColumnCount(7)
        self.ui.add_task_button.clicked.connect(self.add_task)
        self.ui.sort_tasks_button.clicked.connect(self.sort_tasks)
        self.ui.task_table.itemChanged.connect(self.handle_item_change)
        self.delete_mapper = QSignalMapper(self)
        self.delete_mapper.mappedInt.connect(self.delete_task)

        self.more_mapper = QSignalMapper(self)
        self.more_mapper.mappedInt.connect(self.show_task_details)

        self.load_data(order_by_id=True)

    def load_data(self, order_by_id=False):
        self.ui.task_table.setRowCount(0)
        tasks = get_tasks()
        if order_by_id:
            tasks.sort(key=lambda x: x[0])
        for row_num, task in enumerate(tasks):
            self.ui.task_table.insertRow(row_num)
            for col_num, data in enumerate(task):
                if col_num == 5:
                    item = QTableWidgetItem()
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                    item.setCheckState(Qt.Checked if data == 1 else Qt.Unchecked)
                    self.ui.task_table.setItem(row_num, col_num, item)
                else:
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter)
                    if col_num == 4 and data == "High":
                        item.setBackground(Qt.red)
                    self.ui.task_table.setItem(row_num, col_num, item)
            self.add_actions_buttons(row_num)

    def add_actions_buttons(self, row):
        container_widget = QWidget()
        layout = QHBoxLayout(container_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        delete_button = QPushButton("Delete")
        layout.addWidget(delete_button)
        self.delete_mapper.setMapping(delete_button, row)
        delete_button.clicked.connect(self.delete_mapper.map)

        more_button = QPushButton("More")
        layout.addWidget(more_button)
        self.more_mapper.setMapping(more_button, row)
        more_button.clicked.connect(self.more_mapper.map)

        self.ui.task_table.setCellWidget(row, 6, container_widget)

    def add_task(self):
        title = self.ui.title_input.text()
        description = self.ui.description_input.text()
        time = self.ui.time_input.text()
        priority = self.ui.priority_input.currentText()
        add_task(title, description, time, priority)
        self.ui.title_input.clear()
        self.ui.description_input.clear()
        self.ui.priority_input.setCurrentText("Normal")
        self.load_data(order_by_id=True)

    def handle_item_change(self, item):
        if item.column() == 5:
            task_id = self.ui.task_table.item(item.row(), 0).text()
            done = item.checkState() == Qt.Checked
            update_task_done(task_id, done)

    def delete_task(self, row):
        task_id = self.ui.task_table.item(row, 0).text()
        delete_task(task_id)
        self.load_data(order_by_id=True)

    def show_task_details(self, row):
        title = self.ui.task_table.item(row, 1).text()
        description = self.ui.task_table.item(row, 2).text()
        time = self.ui.task_table.item(row, 3).text()
        done_item = self.ui.task_table.item(row, 5)
        done_status = "✔️" if done_item and done_item.checkState() == Qt.Checked else "❌"
        QMessageBox.information(
            self, 
            "Task Details", 
            f"Title: {title}\nDescription: {description}\nTime: {time}\nDone: {done_status}"
        )

    def sort_tasks(self):
        tasks = get_tasks()
        tasks.sort(key=lambda x: (x[5], x[0]))
        self.ui.task_table.setRowCount(0)
        for row_num, task in enumerate(tasks):
            self.ui.task_table.insertRow(row_num)
            for col_num, data in enumerate(task):
                item = QTableWidgetItem(str(data))
                item.setTextAlignment(Qt.AlignCenter)
                if col_num == 5:
                    item.setCheckState(Qt.Checked if data else Qt.Unchecked)
                if col_num == 4 and data == "High":
                    item.setBackground(Qt.red)
                self.ui.task_table.setItem(row_num, col_num, item)
            self.add_actions_buttons(row_num)

if __name__ == "__main__":
    create_table()
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
