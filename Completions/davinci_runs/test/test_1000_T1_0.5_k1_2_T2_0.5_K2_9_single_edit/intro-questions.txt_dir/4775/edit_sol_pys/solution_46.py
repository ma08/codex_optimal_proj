

a, b = [input() for _ in range(2)]

for i in range(len(b)):
    for j in range(len(a)):
        if a[j] == b[i]:
            print(b[i], end='')
        else:
            print('.', end='')
    print()
