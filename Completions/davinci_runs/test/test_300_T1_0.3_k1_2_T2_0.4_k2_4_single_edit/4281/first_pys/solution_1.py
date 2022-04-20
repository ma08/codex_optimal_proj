

n = int(input())
x = list(map(int, input().split()))

min_houses = max(x) - min(x) + 1
max_houses = n

for i in range(n):
    if x[i] == 1:
        max_houses -= 1
    if x[i] == n:
        max_houses -= 1

print(min_houses, max_houses)