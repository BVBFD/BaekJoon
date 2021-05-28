t = int(input("몇 초의 전자레인지 조리 시간이 필요하십니까? : "))
a = 0
b = 0
c = 0

if t % 10 != 0 or t < 1 or t > 10000:
    print(-1)

else:
    while t != 1:

        if int(t/300) != 0:
            a = int(t/300)
            t -= 300*a

        elif int(t/60) != 0:
            b = int(t/60)
            t -= 60*b

        elif int(t/10) != 0:
            c = int(t/10)
            t -= 10*c

        else:
            print("A버튼 {0}번, B버튼 {1}번, C버튼 {2}번 누르세요".format(a, b, c))
            break
