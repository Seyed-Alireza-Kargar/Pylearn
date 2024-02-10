from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
import math


def add():
    global a
    a = float(main_window.txtbox.text())
    main_window.txtbox.setText("")
    main_window.txtbox_2.setText(f"{str(int(a)) if a.is_integer() else str(a)} + ")


def subtract():
    global a
    a = float(main_window.txtbox.text())
    main_window.txtbox.setText("")
    main_window.txtbox_2.setText(f"{str(int(a)) if a.is_integer() else str(a)} - ")


def multiply():
    global a
    a = float(main_window.txtbox.text())
    main_window.txtbox.setText("")
    main_window.txtbox_2.setText(f"{str(int(a)) if a.is_integer() else str(a)} × ")


def divide():
    global a
    a = float(main_window.txtbox.text())
    main_window.txtbox.setText("")
    main_window.txtbox_2.setText(f"{str(int(a)) if a.is_integer() else str(a)} ÷ ")


def result():

    b = float(main_window.txtbox.text())
    if "+" in main_window.txtbox_2.text():
        c = a + b
        op = "+"
    elif "-" in main_window.txtbox_2.text():
        c = a - b
        op = "-"
    elif "×" in main_window.txtbox_2.text():
        c = a * b
        op = "×"
    elif "÷" in main_window.txtbox_2.text():
        if b != 0:
            c = a / b
            op = "÷"
        else:
            main_window.txtbox.setText("Error")
            return

    result_text = f"= {str(int(c)) if c.is_integer() else str(c)}"
    main_window.txtbox.setText(result_text)
    main_window.txtbox_2.setText(f"{str(int(a)) if a.is_integer() else str(a)} {main_window.txtbox_2.text().split(' ')[-1]}{op} {str(int(b)) if b.is_integer() else str(b)}")


def num(x):
    old_number = main_window.txtbox.text()
    new_number = old_number + x
    main_window.txtbox.setText(new_number)


def ac():
    main_window.txtbox.setText("")
    main_window.txtbox_2.setText("")


def dele():
    text = main_window.txtbox.text()
    res = int(text) // 10
    if res == 0 :
        main_window.txtbox.setText("")
    else :
        main_window.txtbox.setText(str(res))
        


def calculate_sin():
    num = float(main_window.txtbox.text())
    result = math.sin(math.radians(num))
    display_result(result, "sin")

def calculate_cos():
    num = float(main_window.txtbox.text())
    result = math.cos(math.radians(num))
    display_result(result, "cos")

def calculate_tan():
    num = float(main_window.txtbox.text())
    result = math.tan(math.radians(num))
    display_result(result, "tan")

def calculate_cot():
    num = float(main_window.txtbox.text())
    result = 1 / math.tan(math.radians(num))
    display_result(result, "cot")

def calculate_sqrt():
    num = float(main_window.txtbox.text())
    result = math.sqrt(num)
    display_result(result, "sqrt")

def calculate_log():
    num = float(main_window.txtbox.text())
    result = math.log10(num)
    display_result(result, "log")

def display_result(result, operation):
    main_window.txtbox.setText(f"{operation}({main_window.txtbox.text()}) = {str(int(result)) if result.is_integer() else str(result)}")
    main_window.txtbox_2.setText("")



app = QApplication([])

loader = QUiLoader()
main_window = loader.load("17/Calculator.ui")
main_window.show()

main_window.btn_equal.clicked.connect(result)
main_window.btn_sum.clicked.connect(add)
main_window.btn_sub.clicked.connect(subtract)
main_window.btn_mul.clicked.connect(multiply)
main_window.btn_div.clicked.connect(divide)
main_window.btn_num_1.clicked.connect(partial(num, "1"))
main_window.btn_num_2.clicked.connect(partial(num, "2"))
main_window.btn_num_3.clicked.connect(partial(num, "3"))
main_window.btn_num_4.clicked.connect(partial(num, "4"))
main_window.btn_num_5.clicked.connect(partial(num, "5"))
main_window.btn_num_6.clicked.connect(partial(num, "6"))
main_window.btn_num_7.clicked.connect(partial(num, "7"))
main_window.btn_num_8.clicked.connect(partial(num, "8"))
main_window.btn_num_9.clicked.connect(partial(num, "9"))
main_window.btn_num_0.clicked.connect(partial(num, "0"))
main_window.btn_pt.clicked.connect(partial(num, "."))
main_window.btn_ac.clicked.connect(ac)
main_window.btn_del.clicked.connect(dele)
main_window.btn_sin.clicked.connect(calculate_sin)
main_window.btn_cos.clicked.connect(calculate_cos)
main_window.btn_tan.clicked.connect(calculate_tan)
main_window.btn_cot.clicked.connect(calculate_cot)
main_window.btn_sqrt.clicked.connect(calculate_sqrt)
main_window.btn_log.clicked.connect(calculate_log)

app.exec()
