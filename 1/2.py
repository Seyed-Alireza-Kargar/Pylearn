num1 = input("enter num 1 : ")
num2 = input("enter num 2 : ")
num3 = input("enter num 3 : ")

if num1+num2 <= num3 or num1 + num3 <= num2 or num2 + num3 <= num1 :
    print("no")
else:
    print("yes")