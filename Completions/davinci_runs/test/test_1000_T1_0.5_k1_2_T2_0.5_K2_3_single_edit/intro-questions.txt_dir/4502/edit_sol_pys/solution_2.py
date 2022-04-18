
n = input()
a = []
for i in range(int(n)):
    a.append(int(input()))
    a.sort()
    if len(a) % 2 == 0:
        print((a[len(a) // 2 - 1] + a[len(a) // 2]) / 2)
    else:
        print(a[len(a) // 2])
