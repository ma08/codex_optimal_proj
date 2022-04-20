


n = int(input())
x = list(map(int, input().split()))

min_houses = 1
max_houses = 1

for i in range(n):
    if i == 0:
        if x[i] != x[i + 1]:
            min_houses += 1
    elif i == n - 1:
        if x[i] != x[i - 1]:
            min_houses += 1
    else:
        if x[i] != x[i - 1] and x[i] != x[i + 1]:
            min_houses += 1

for i in range(n):
    if i == 0 and x[i] == 1:
        max_houses += 1
    elif i == n - 1 and x[i] == n:
        max_houses += 1
    elif i != 0 and i != n - 1:
        if x[i] == 1 and x[i - 1] != 1:
            max_houses += 1
        if x[i] == n and x[i + 1] != n:
            max_houses += 1

print(min_houses, max_houses)