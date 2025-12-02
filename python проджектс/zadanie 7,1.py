k = int(input())
if k >= 5 and (k % 5 == 0 or k % 7 == 0 or k % 5 == 2 or k % 7 == 5 or (k >= 12 and k != 13 and k != 16 and k != 18 and k != 23)):
    print("да")
else:
    print("нет")