A, B = map(int,input().split("x"))
C, D, E = map(int,input().split("x"))
if A >= C or A >= D or A >= E and B >= C or B >= D or B >= E:
    print("да")
else:
    print("нет")