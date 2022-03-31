n = int(input())
a = []
for i in range(2 * n - 2):
    a.append(input())

ans = []
for i in range(2 * n - 2):
    if a[i] not in ans:
        ans.append(a[i])

for i in range(2 * n - 2):
    if a[i] in ans:
        print("P", end="")
        ans.remove(a[i])
    else:
        print("S", end="")
