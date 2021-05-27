a = int(input("반복횟수를 입력하세요 : "))

for i in range(a):
    for n in range(i+1):
        print("*", end="")
    print("")
