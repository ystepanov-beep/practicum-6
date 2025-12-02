length, width = map(int,input().split("x"))
if 0 <= (length**2 + width**2)**0.5 <= 13:
    print("да")
else:
    print("нет")