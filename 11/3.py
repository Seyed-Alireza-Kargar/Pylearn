class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        result = ComplexNumber(real_part, imaginary_part)
        return result

    def multiply(self, other):
        real_part = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginary_part = (self.real * other.imaginary) + (self.imaginary * other.real)
        result = ComplexNumber(real_part, imaginary_part)
        return result

    def subtract(self, other):
        real_part = self.real - other.real
        imaginary_part = self.imaginary - other.imaginary
        result = ComplexNumber(real_part, imaginary_part)
        return result

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

num1 = ComplexNumber(3, 4)
num2 = ComplexNumber(1, 2)

result_add = num1.add(num2)
print(f"sum: {num1} + {num2} = {result_add}")

result_multiply = num1.multiply(num2)
print(f"mul: {num1} x {num2} = {result_multiply}")

result_subtract = num1.subtract(num2)
print(f"sub: {num1} - {num2} = {result_subtract}")
