n = int(input())
a = list(map(int, input().split()))


# n = 4
# a = [1, 2, 3, 4]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if a[i] == a[j] or a[j] == a[k] or a[k] == a[i]:
                continue
            if a[i] + a[j] == a[k] or a[i] + a[k] == a[j] or a[j] + a[k] == a[i]:
                print("Yes")
                exit()
print("No")
