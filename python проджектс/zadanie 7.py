k = int(input())
found = False
for five in range(k // 5 + 1):
    for seven in range(k // 7 + 1):
        if five * 5 + seven * 7 == k:
            found = True
            break
print("да" if found else "нет")