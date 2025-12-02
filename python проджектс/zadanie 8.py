N = int(input())
if N <= 10:
    print(N - 1)
if 11 <= N <= 190 and N % 2 == 1 and N % 20 > 10:
    print(N // 20 + 1)
elif 11 <= N <= 190 and N % 2 == 1 and N % 20 < 10:
    print(N // 20)
if 11 <= N <= 190 and N % 2 == 0 and N % 10 != 0 and (N - 10) % 20 <= 10:
    print(N % 10 // 2 - 1)
elif 11 <= N <= 190 and N % 10 == 0:
    print(4 + (N % 20 // 2))
elif 11<= N <= 190 and N % 2 == 0 and (N - 10) % 20 >= 10:
    print(N % 10 // 2 + 4)
if 191 <= N <= 492 and N % 3 == 2:
    print(1)
if 191 <= N <= 492 and N % 3 == 1:
    print((N - 193) // 3 % 10)
if 191 <= N <= 492 and N % 3 == 0:
    print((N - 192) // 30)
if N == 493:
    print(2)
if N == 494:
    print(0)
if N == 495:
    print(0)