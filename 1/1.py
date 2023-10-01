# ----- Calculator -----
import math

print("Coercion: 1 \nGeometry : 2 \nFactorial : 3")
chooses = int(input("please enter yor choose : "))
print()
result = 0

if chooses == 1:
    print("plus : +\nminus : -\ntimes : *\ndivision : /\npow : **\nsqrt : #(for example --> input : 4 # | output : 2)")

    print()
    input = input("please enter your operation : ")

    num1 = 0
    num2 = 0
    indexes = input.split(' ')

    operator = indexes[1]
    errors = False
    num1 = float(indexes[0])
    if len(indexes) == 3:
        num2 = float(indexes[2])


    if operator == '+' :
        result = num1 + num2
    elif operator == '-' :
        result = num1 - num2
    elif operator == '*' :
        result = num1 * num2
    elif operator == '/' :
        if num2 == 0:
            errors = True
            print("Dividing by 0 is not possible")
        else:
            result = num1 / num2
    elif operator == "**" :
        result = num1 ** num2
    elif operator == "#":
        result = num1 ** 0.5

elif chooses == 2 :
    print("sin \ncos \ntan \ncot")

    print()
    input = input("please enter your operator and degree : ")
    indexes = input.split(' ')
    degree = float(indexes[1])

    radian = degree * (math.pi / 180.0)

    if indexes[0] == 'sin' :
        result = math.sin(radian)
    elif indexes[0] == 'cos' :
        result = math.cos(radian)
    elif indexes[0] == 'tan' :
        result = math.tan(radian)
    elif indexes[0] == 'cot' :
        result = math.cot(radian)

elif chooses == 3:
    print()
    input = input("please enter your number : ")
    fact = 1
    for i in range(1, int(input)+1):
        fact *= i
    
    result = fact


print(result)



