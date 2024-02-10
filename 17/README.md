## Calculator App

This simple calculator application is implemented in Python using PySide6 for the graphical user interface. The calculator supports basic arithmetic operations, trigonometric functions, square root, and logarithm.

![Calculator App](screenshot.png)

### Requirements

To run the calculator, you need to have Python installed on your machine. Additionally, you need to install the PySide6 library. You can install it using the following command:

```bash
pip install PySide6
```

### How to Run

1. Clone the repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run the calculator by executing the following command:

```bash
python calculator.py
```

### User Interface

The graphical user interface (GUI) of the calculator is created using Qt Designer, and the UI file is loaded using the QUiLoader class. The calculator interface includes buttons for digits, arithmetic operations, and various mathematical functions.

![Calculator App](calculator_app_screenshot.png)

### Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division.
- **Trigonometric Functions**: Sine, cosine, tangent, and cotangent.
- **Other Mathematical Functions**: Square root and logarithm.

### Usage

1. Enter numbers using the numeric buttons (0-9).
2. Perform basic arithmetic operations by clicking the corresponding buttons (+, -, ×, ÷).
3. Use the "AC" button to clear the input.
4. Delete the last entered digit with the "DEL" button.
5. Calculate trigonometric functions, square root, and logarithm using the dedicated buttons.
6. Press the "=" button to display the result.

### References

- [PySide6 Documentation](https://doc.qt.io/qtforpython/)

### Notes

- The calculator uses the `math` module for trigonometric functions, square root, and logarithm.
- The GUI layout is designed using the Qt Designer tool.

Feel free to explore, modify, and enhance the calculator application based on your needs!
