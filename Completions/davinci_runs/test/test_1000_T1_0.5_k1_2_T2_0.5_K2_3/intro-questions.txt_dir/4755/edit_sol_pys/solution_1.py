n = int(input())
i = 1
while n >= i:
    if i % 3 == 0 or i % 5 == 0:
        i += 1
        continue
    print(i)
    i += 1
