

k = int(input())

i = 1
while True:
    if (7 * (10 ** i)) % k == 0:
        print(i + 1)
        break
    i += 1