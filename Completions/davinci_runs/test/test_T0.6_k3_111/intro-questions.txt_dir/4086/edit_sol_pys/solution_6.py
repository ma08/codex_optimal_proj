n = int(input())
a = list(map(int, input().split()))  # a = [1, 2, 3, 4, 5, 6]
b = []  # b = []
c = []  # c = []

for i in range(n):
    if a[i] not in b:  # a[0] = 1 not in b
        b.append(a[i])  # b = [1]
        c.append(i)  # c = [0]
    else:
        continue

x = len(b)  # x = 1
print(x)  # 1
for j in range(x):  # j = 0
    print(a[c[j]], end=' ')  # a[0] = 1
