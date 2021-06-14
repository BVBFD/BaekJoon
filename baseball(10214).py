from random import *

t = int(input("테스트 케이스 경기 수를 입력해주세요 : "))
list_k = []
list_y = []
sum_k = 0
sum_y = 0

for i in range(1, t + 1):
    print(i)
    for n in range(1, 10):
        k = randint(1, 9)
        y = randint(1, 9)
        print("{0} {1}".format(k, y))
        list_k.append(k)
        list_y.append(y)
    for k in list_k:
        k = + k
        sum_k = k

    for y in list_y:
        y = + y
        sum_y = y

    if sum_k > sum_y:
        print("Korea")
    elif sum_k < sum_y:
        print("Yonsei")
    else:
        print("Draw")
