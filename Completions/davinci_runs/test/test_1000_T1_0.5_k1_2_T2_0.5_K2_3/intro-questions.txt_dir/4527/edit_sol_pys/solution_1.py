

# Activity Selection Problem

t = int(input())

for _ in range(t):
    n = int(input())
    a = []
    for __ in range(n):
        a.append(list(map(int, input().split())))
    a.sort(key=lambda x: x[1])
    count = 0
    j = 0
    for i in range(n):
        if a[i][0] >= a[j][1]:
            count += 1
            j = i
    print(count)
