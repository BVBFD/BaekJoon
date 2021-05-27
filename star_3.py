a = int(input("반복 횟수를 입력하세요 : "))

for i in range(a, 0, -1):
    for n in range(i):
        print("*", end="")
    print("")
