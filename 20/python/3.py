import random

scores = {"user": 0, "computer1": 0, "computer2": 0}

i = 5
while i > 0:
    while True:
        user_choose = int(input("Please Enter Your Choose (1 = ✋ / 2 = 🤚) : "))
        if user_choose != 1 and user_choose != 2:
            print(f"{user_choose} is not valid !!")
            print("Please Enter 1 or 2 !!!")
            continue
        break

    computer1_choose = random.randint(1,2)
    computer2_choose = random.randint(1,2)

    if user_choose == computer1_choose != computer2_choose:
        scores["computer2"] += 1
        print("computer2 win!!")
    elif user_choose == computer2_choose != computer1_choose:
        scores["computer1"] += 1
        print("computer1 win!!")
    elif computer1_choose == computer2_choose != user_choose:
        scores["user"] += 1
        print("user win!!")
    else:
        print("draw!!")
    
    print()


    i -= 1

max_score = max(scores.values())
max_keys = [key for key, value in scores.items() if value == max_score]

print()
print("-------------------------------------------")
print()
print("max score : ")
for key in max_keys:
    print(key, ":", max_score)
