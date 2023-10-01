timeInput = input("enter time : ")

timeSplit = timeInput.split(':')

sum = (int(timeSplit[0]) * 60 * 60) + (int(timeSplit[1]) * 60) + (int(timeSplit[2]))

print(sum)