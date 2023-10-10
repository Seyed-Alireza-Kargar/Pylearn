def solve_cubic_equation(a, b, c, d):
    p = (3 * a * c - b**2) / (3 * a**2)
    q = (2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / (27 * a**3)
    delta = (q / 2)**2 + (p / 3)**3

    if delta >= 0:
        A = (-q / 2 + delta**0.5)**(1/3)
        B = (-q / 2 - delta**0.5)**(1/3)
        x1 = A + B - b / (3 * a)
        return [x1]

    else:
        r = ((q / 2)**2 + abs(delta))**0.5
        theta = sp.acos(-q / (2 * r))
        x1 = 2 * (r**(1/3)) * sp.cos(theta / 3) - b / (3 * a)
        x2 = 2 * (r**(1/3)) * sp.cos((theta + 2 * sp.pi) / 3) - b / (3 * a)
        x3 = 2 * (r**(1/3)) * sp.cos((theta + 4 * sp.pi) / 3) - b / (3 * a)
        return [x1, x2, x3]


a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))
d = float(input("d : "))

solutions = solve_cubic_equation(a, b, c, d)
print("ریشه‌های معادله:")
print(solutions)
