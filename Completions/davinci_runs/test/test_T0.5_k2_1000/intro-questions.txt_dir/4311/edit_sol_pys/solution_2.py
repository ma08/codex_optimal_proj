s = int(input())
a = [s]

while True:
    if a[-1] % 2 == 0:
        a.append(int(a[-1] / 2))
    else:
        a.append(int(3 * a[-1] + 1))
    if a.count(a[-1]) == 2:
        print(a.index(a[-1]) + 1)
        break
