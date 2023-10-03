import random
import time



while True:
    gift1 = 6
    gift2 = 6
    dice_result = random.randint(1, 6)

    print(f'انداخته‌شده: {dice_result}')

    time.sleep(2)
    if dice_result == 6:
        print(f'تبریک! عدد 6 آمد.')
        rolls = 0

        while gift1 == 6 or gift2 == 6 :
            gift1 = random.randint(1, 6)
            print(f"جایزه اول : {gift1}")
            gift2 = random.randint(1, 6)
            print(f"جایزه دوم : {gift2}")
    else:
        continue
