num1 = int(input("لطفا عدد اول را وارد کنید: "))
num2 = int(input("لطفا عدد دوم را وارد کنید: "))

min_num = min(num1, num2)

lcm_result = 0
for i in range(min_num, num1 * num2 + 1):
    if i % num1 == 0 and i % num2 == 0:
        lcm_result = i
        break

print(f"ک.م.م عدد {num1} و {num2} برابر است با: {lcm_result}")
