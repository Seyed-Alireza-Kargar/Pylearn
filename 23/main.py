import sys
import random
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtGui import QColor, QPalette
from PySide6.QtCore import Qt
from main_window import Ui_MainWindow
from sudoku import Sudoku

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dark_mode = False
        self.solved = False
        self.solved_puzzle = None

        self.ui.menu_new.triggered.connect(self.new_game)
        self.ui.menu_open_file.triggered.connect(self.open_file)
        self.ui.menu_about.triggered.connect(self.show_about)
        self.ui.menu_help.triggered.connect(self.show_help)
        self.ui.menu_exit.triggered.connect(self.close)
        self.ui.menu_solve.triggered.connect(self.solve_game)
        self.ui.dark_mode_button.clicked.connect(self.toggle_dark_mode)

        self.line_edit = [[None for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                new_cell.setAlignment(Qt.AlignCenter)
                new_cell.setFixedSize(50, 50)
                self.ui.grid_layout.addWidget(new_cell, i, j)
                new_cell.textChanged.connect(partial(self.validation, i, j))
                self.line_edit[i][j] = new_cell

        self.add_grid_lines()

        self.new_game()
    
    def add_grid_lines(self):
        for i in range(1, 9):
            if i % 3 == 0:
                line = QLabel()
                line.setFixedHeight(2)
                line.setStyleSheet("background-color: black;")
                self.ui.grid_layout.addWidget(line, i, 0, 0, 9)

        for j in range(1, 9):
            if j % 3 == 0:
                line = QLabel()
                line.setFixedWidth(2)
                line.setStyleSheet("background-color: black;")
                self.ui.grid_layout.addWidget(line, 0, j, 9, 1)

    def open_file(self):
        try:
            file_path = QFileDialog.getOpenFileName(self, "Open File ...")[0]
            if not file_path:
                return
            
            with open(file_path, "r") as f:
                big_text = f.read()
            rows = big_text.strip().split("\n")
            puzzle_board = [[int(cells) for cells in row.split(" ")] for row in rows]

            for i in range(9):
                for j in range(9):
                    if puzzle_board[i][j] != 0:
                        self.line_edit[i][j].setText(str(puzzle_board[i][j]))
                        self.line_edit[i][j].setReadOnly(True)
                    else:
                        self.line_edit[i][j].clear()
                        self.line_edit[i][j].setReadOnly(False)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load file: {str(e)}")

    def new_game(self):
        self.solved = False
        puzzle = Sudoku(3, seed=random.randint(1, 1000)).difficulty(0.5)
        self.solved_puzzle = puzzle.solve().board
        for i in range(9):
            for j in range(9):
                self.line_edit[i][j].setStyleSheet("")
                if puzzle.board[i][j] is not None:
                    self.line_edit[i][j].setText(str(puzzle.board[i][j]))
                    self.line_edit[i][j].setReadOnly(True)
                else:
                    self.line_edit[i][j].clear()
                    self.line_edit[i][j].setReadOnly(False)

    def validation(self, i, j, text):
        if text not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.line_edit[i][j].setText("")
        self.check_board()

    def check_board(self):
        if self.solved:
            return

        valid = True
        for i in range(9):
            for j in range(9):
                self.line_edit[i][j].setStyleSheet("")

        for i in range(9):
            if not self.check_line([self.line_edit[i][j].text() for j in range(9)], i, 'row'):
                valid = False

        for j in range(9):
            if not self.check_line([self.line_edit[i][j].text() for i in range(9)], j, 'col'):
                valid = False

        for bi in range(3):
            for bj in range(3):
                block = [self.line_edit[i][j].text() for i in range(bi*3, bi*3 + 3) for j in range(bj*3, bj*3 + 3)]
                if not self.check_block(block, bi, bj):
                    valid = False

        if valid and all(self.line_edit[i][j].text() for i in range(9) for j in range(9)):
            QMessageBox.information(self, "Congratulations", "You have completed the puzzle! 🎉")
            self.new_game()

    def check_line(self, line, index, mode):
        seen = set()
        for idx, num in enumerate(line):
            if num in seen:
                for j in range(9):
                    if mode == 'row' and self.line_edit[index][j].text() == num:
                        self.line_edit[index][j].setStyleSheet("background-color: red")
                    if mode == 'col' and self.line_edit[j][index].text() == num:
                        self.line_edit[j][index].setStyleSheet("background-color: red")
                return False
            if num != "":
                seen.add(num)
        return True

    def check_block(self, block, bi, bj):
        seen = set()
        for idx, num in enumerate(block):
            if num in seen:
                for i in range(bi*3, bi*3 + 3):
                    for j in range(bj*3, bj*3 + 3):
                        if self.line_edit[i][j].text() == num:
                            self.line_edit[i][j].setStyleSheet("background-color: red")
                return False
            if num != "":
                seen.add(num)
        return True

    def show_about(self):
        QMessageBox.information(self, "About", "Sudoku Game\nCreated by Alireza\nFor Pylearn Course")

    def show_help(self):
        QMessageBox.information(self, "Help", "Fill the grid with numbers 1 to 9.\nNo repeats in any row, column, or 3x3 block.")

    def solve_game(self):
        self.solved = True
        for i in range(9):
            for j in range(9):
                if not self.line_edit[i][j].text():
                    self.line_edit[i][j].setText(str(self.solved_puzzle[i][j]))
                    self.line_edit[i][j].setStyleSheet("background-color: lightgreen; color: black;")
                    self.line_edit[i][j].setReadOnly(True)

    def toggle_dark_mode(self):
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)

        if self.dark_mode:
            app.setPalette(QApplication.style().standardPalette())
        else:
            app.setPalette(dark_palette)

        self.dark_mode = not self.dark_mode


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec())
