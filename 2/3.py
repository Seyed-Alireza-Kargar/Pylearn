score = '0'
sum = 0
num = 0
while score != 'exit':
    score = input("enter score : ")
    if score != 'exit':
        sum += float(score)
        num += 1

ave = sum / num

print(ave)