from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
import math


class CalculatorApp:
    def __init__(self):
        self.a = None

        self.app = QApplication([])
        self.loader = QUiLoader()
        self.main_window = self.loader.load("17/Calculator.ui")

        self.connect_buttons()

    def connect_buttons(self):
        self.main_window.btn_equal.clicked.connect(self.result)
        self.main_window.btn_sum.clicked.connect(self.add)
        self.main_window.btn_sub.clicked.connect(self.subtract)
        self.main_window.btn_mul.clicked.connect(self.multiply)
        self.main_window.btn_div.clicked.connect(self.divide)
        self.main_window.btn_num_1.clicked.connect(partial(self.num, "1"))
        self.main_window.btn_num_2.clicked.connect(partial(self.num, "2"))
        self.main_window.btn_num_3.clicked.connect(partial(self.num, "3"))
        self.main_window.btn_num_4.clicked.connect(partial(self.num, "4"))
        self.main_window.btn_num_5.clicked.connect(partial(self.num, "5"))
        self.main_window.btn_num_6.clicked.connect(partial(self.num, "6"))
        self.main_window.btn_num_7.clicked.connect(partial(self.num, "7"))
        self.main_window.btn_num_8.clicked.connect(partial(self.num, "8"))
        self.main_window.btn_num_9.clicked.connect(partial(self.num, "9"))
        self.main_window.btn_num_0.clicked.connect(partial(self.num, "0"))
        self.main_window.btn_pt.clicked.connect(partial(self.num, "."))
        self.main_window.btn_ac.clicked.connect(self.ac)
        self.main_window.btn_del.clicked.connect(self.dele)
        self.main_window.btn_sin.clicked.connect(self.calculate_sin)
        self.main_window.btn_cos.clicked.connect(self.calculate_cos)
        self.main_window.btn_tan.clicked.connect(self.calculate_tan)
        self.main_window.btn_cot.clicked.connect(self.calculate_cot)
        self.main_window.btn_sqrt.clicked.connect(self.calculate_sqrt)
        self.main_window.btn_log.clicked.connect(self.calculate_log)

    def run(self):
        self.main_window.show()
        self.app.exec()

    def add(self):
        self.a = float(self.main_window.txtbox.text())
        self.clear_textboxes()
        self.main_window.txtbox_2.setText(f"{str(int(self.a)) if self.a.is_integer() else str(self.a)} + ")

    def subtract(self):
        self.a = float(self.main_window.txtbox.text())
        self.clear_textboxes()
        self.main_window.txtbox_2.setText(f"{str(int(self.a)) if self.a.is_integer() else str(self.a)} - ")

    def multiply(self):
        self.a = float(self.main_window.txtbox.text())
        self.clear_textboxes()
        self.main_window.txtbox_2.setText(f"{str(int(self.a)) if self.a.is_integer() else str(self.a)} × ")

    def divide(self):
        self.a = float(self.main_window.txtbox.text())
        self.clear_textboxes()
        self.main_window.txtbox_2.setText(f"{str(int(self.a)) if self.a.is_integer() else str(self.a)} ÷ ")

    def result(self):
        b = float(self.main_window.txtbox.text())
        if "+" in self.main_window.txtbox_2.text():
            c = self.a + b
            op = "+"
        elif "-" in self.main_window.txtbox_2.text():
            c = self.a - b
            op = "-"
        elif "×" in self.main_window.txtbox_2.text():
            c = self.a * b
            op = "×"
        elif "÷" in self.main_window.txtbox_2.text():
            if b != 0:
                c = self.a / b
                op = "÷"
            else:
                self.main_window.txtbox.setText("Error")
                return

        result_text = f"= {str(int(c)) if c.is_integer() else str(c)}"
        self.main_window.txtbox.setText(result_text)
        self.main_window.txtbox_2.setText(
            f"{str(int(self.a)) if self.a.is_integer() else str(self.a)} {self.main_window.txtbox_2.text().split(' ')[-1]}{op} {str(int(b)) if b.is_integer() else str(b)}")

    def num(self, x):
        old_number = self.main_window.txtbox.text()
        new_number = old_number + x
        self.main_window.txtbox.setText(new_number)

    def ac(self):
        self.clear_textboxes()

    def dele(self):
        text = self.main_window.txtbox.text()
        res = int(text) // 10
        self.main_window.txtbox.setText("") if res == 0 else self.main_window.txtbox.setText(str(res))

    def clear_textboxes(self):
        self.main_window.txtbox.setText("")
        self.main_window.txtbox_2.setText("")

    def calculate_sin(self):
        num = float(self.main_window.txtbox.text())
        result = math.sin(math.radians(num))
        self.display_result(result, "sin")

    def calculate_cos(self):
        num = float(self.main_window.txtbox.text())
        result = math.cos(math.radians(num))
        self.display_result(result, "cos")

    def calculate_tan(self):
        num = float(self.main_window.txtbox.text())
        result = math.tan(math.radians(num))
        self.display_result(result, "tan")

    def calculate_cot(self):
        num = float(self.main_window.txtbox.text())
        result = 1 / math.tan(math.radians(num))
        self.display_result(result, "cot")

    def calculate_sqrt(self):
        num = float(self.main_window.txtbox.text())
        result = math.sqrt(num)
        self.display_result(result, "sqrt")

    def calculate_log(self):
        num = float(self.main_window.txtbox.text())
        result = math.log10(num)
        self.display_result(result, "log")

    def display_result(self, result, operation):
        self.main_window.txtbox.setText(
            f"{operation}({self.main_window.txtbox.text()}) = {str(int(result)) if result.is_integer() else str(result)}")
        self.main_window.txtbox_2.setText()


if __name__ == "__main__":
    calculator_app = CalculatorApp()
    calculator_app.run()
