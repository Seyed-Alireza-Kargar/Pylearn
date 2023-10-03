timeinput = int(input("please enter second : "))

h = 0
m = timeinput // 60
s = timeinput % 60
if m // 60 >= 1 :
    h += m // 60
    m -= h * 60

print(f"{int(h)} : {int(m)} : {int(s)}")