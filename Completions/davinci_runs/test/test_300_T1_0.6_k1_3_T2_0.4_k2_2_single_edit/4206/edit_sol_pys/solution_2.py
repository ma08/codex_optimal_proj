

n = input()

if len(n) == 1:
    print(1)
else:
    count = 0
    for i in range(1, len(n)):
        if int(n[:i]) % 3 == 0:
            count += 1
    print(count)
