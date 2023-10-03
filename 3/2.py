import random

n = int(input("تعداد عناصر آرایه را وارد کنید: "))


initial_list = list(range(1, n+1))
print(initial_list)

selected_items = random.sample(initial_list, min(n, n))

print(selected_items)
