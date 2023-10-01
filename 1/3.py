name = input("Enter name : ")

sum = 1
lesson = {"l1" : [], "l2" : [], "l3" : []}
while sum <= 3:
    lesson_name = input("lesson name : ")
    lesson_score = float(input("lesson score : "))
    lesson[f"l{sum}"].append(lesson_score)

    sum += 1

sum_score = 0
for item in lesson.values():
    sum_score += item[0]

average = sum_score / 3

if average >= 17 :
    print(f"{name} is average : {average} | you are Great")
elif 17 > average >= 12 :
    print(f"{name} is average : {average} | you are Normal ")
else:
    print(f"{name} is average : {average} | you are Fail")