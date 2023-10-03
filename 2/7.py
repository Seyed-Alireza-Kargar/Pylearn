def fibonacci_sequence(n):
    if n <= 0:
        print("تعداد عناصر باید بزرگتر از صفر باشد.")
        return
    elif n == 1:
        print("1")
        return
    elif n == 2:
        print("1, 1")
        return

    fib_sequence = [1, 1]

    for i in range(2, n):
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    print(', '.join(map(str, fib_sequence)))

n = int(input("تعداد عناصر دنباله فیبوناچی را وارد کنید: "))

fibonacci_sequence(n)
