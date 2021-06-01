from random import *


def sum_money():
    dice_num = []
    for i in range(0, 3):
        a = int(randint(1, 6))
        dice_num.append(a)

    if dice_num[0] == dice_num[1] and dice_num[1] == dice_num[2] and dice_num[2] == dice_num[0]:
        sum = (dice_num[0]*1000) + 10000
        return sum

    elif dice_num[0] == dice_num[1]:
        sum = (dice_num[0]*2*100) + 1000
        return sum

    elif dice_num[1] == dice_num[2]:
        sum = (dice_num[1]*2*100) + 1000
        return sum

    elif dice_num[2] == dice_num[0]:
        sum = (dice_num[2]*2*100) + 1000
        return sum

    else:
        max_num = max(dice_num)
        sum = max_num*100
        return sum


gamer_num = int(input("게임에 참가하는 선수는 총 몇명입니까? "))

money = []
for i in range(0, gamer_num):
    a = sum_money()
    money.append(a)

print(money)
max_money = max(money)


print("당신이 받게 될 상금은 {0}원 입니다.".format(int(max_money)))
