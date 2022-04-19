
n = int(input())
a = list(map(int, input().split()))

a.sort()
pockets = []

for i in range(len(a)):
    if i == 0:
        pockets.append([a[i]])
    else:
        if a[i] == a[i-1]:
            pockets[-1].append(a[i])
        else:
            pockets.append([a[i]])

print(len(pockets))
