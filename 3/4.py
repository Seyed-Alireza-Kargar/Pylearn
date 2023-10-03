n = int(input("لطفا عدد n را وارد کنید: "))

snake = ""
for i in range(n):
    if i % 2 == 0:
        snake += "*"
    else:
        snake += "#"

print(snake)
