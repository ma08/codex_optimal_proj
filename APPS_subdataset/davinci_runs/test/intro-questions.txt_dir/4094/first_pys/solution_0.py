

K = int(input())

i = 1
while True:
    x = int("7" * i)
    if x % K == 0:
        print(i)
        break
    i += 1