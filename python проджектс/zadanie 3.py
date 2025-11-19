N, M = map(int,input().split("x"))
street = int(input())
if street % N == 0 or street % M == 0 and street < N * M:
    print("успешно")
else:
    print("неосуществимо")