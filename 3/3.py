user_input = input("لطفا اعداد آرایه را وارد کنید (با استفاده از ویرگول جدا کنید): ")
user_array = [int(x) for x in user_input.split(',')]

is_sorted = True
for i in range(len(user_array) - 1):
    if user_array[i] > user_array[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("آرایه مرتب است.")
else:
    print("آرایه مرتب نیست.")
