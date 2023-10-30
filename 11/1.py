import math

class Fraction:
    def __init__(self,  numerator, denominator):
        self.n = numerator
        self.d = denominator

    def sum(self, other):
        result_n = self.n * other.d + self.d * other.n
        result_d = self.d * other.d
        result = Fraction(result_n, result_d)
        return result
    
    def sub(self, other):
        result_n = self.n * other.d - self.d * other.n
        result_d = self.d * other.d
        result = Fraction(result_n, result_d)
        return result


    def mul(self, other):
        result_n = self.n * other.n
        result_d = self.d * other.d
        result = Fraction(result_n, result_d)
        return result
    
    def div(self, other):
        result_n = self.n * other.d
        result_d = self.d * other.n
        result = Fraction(result_n, result_d)
        return result
    
    def frac_to_nymber(self):
        result = self.n / self.d
        return result
    
    def simplify(self):
        bmm = math.gcd(self.n, self.d)
        result_n = int(self.n / bmm)
        result_d = int(self.d / bmm)
        result = Fraction(result_n, result_d)
        return result


    def show(self):
        print(self.n, "/", self.d)



while True:

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Enter + to add Fractions ")
    print("Enter - to subtract fraction ")
    print("Enter * to multiply Fractions ")
    print("Enter / to divide fraction  ")
    print("Enter num to show the fraction as a float number ")
    print("Enter sim to simplify the fraction if it is possible ")
    print("Exit")
    
    operator = input("Choose your operator: ")

    if operator == "Exit":
        break

    elif operator == "num" or operator == "sim":
        a = list(map(int,input("Enter numerator and denominator of the first fraction with a space in between: ").split(" ")))
        frac = Fraction(a[0] , a[1])
        frac.show()

        if operator == "num":
            number = frac.frac_to_nymber()
            print("number: ", number)

        elif operator == "sim":
            simp = frac.simplify()
            simp.show()
    else:
        
        a = list(map(int,input("Enter numerator and denominator of the first fraction with a space in between: ").split(" ")))
        frac1 = Fraction(a[0], a[1])
        frac1.show()

        b = list(map(int, input("Enter numerator and denominator of the first fraction with a space in between: ").split(" ")))
        frac2 = Fraction(b[0], b[1])
        frac2.show()
        

        if operator == "+":
            summ = frac1.sum(frac2)
            summ.show()

        elif operator == "-":
            subb = frac1.sub(frac2)
            subb.show()

        elif operator == "*":
            mull = frac1.mul(frac2)
            mull.show()

        elif operator == "/":
            divv = frac1.div(frac2)
            divv.show()