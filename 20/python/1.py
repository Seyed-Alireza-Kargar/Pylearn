array = [1, 5, 7, 5, 1]

status = False

for item in range(int(len(array) / 2 + 1)):
    if array[item] == array[(item + 1) * -1]:
        status = True
        continue
    else:
        status = False
        break

print(status)