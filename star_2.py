a = int(input("반복 횟수를 입력하세요 : "))

for i in range(1, a + 1):

    for n in range(5-i):
        print(" ", end="")

    for n in range(i):
        print("*", end="")

    print()
