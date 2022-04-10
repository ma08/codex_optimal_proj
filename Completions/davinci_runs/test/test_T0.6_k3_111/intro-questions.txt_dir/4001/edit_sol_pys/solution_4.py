n = int(input())
d = [int(x) for x in input().split()]
d.sort()

if len(d) % 2 == 0:
    print(0)
else:
    print(d[len(d) // 2] - d[len(d) // 2 - 1])
