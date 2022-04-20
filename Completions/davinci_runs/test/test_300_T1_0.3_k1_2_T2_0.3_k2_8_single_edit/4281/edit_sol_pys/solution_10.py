
n = int(input())
x = list(map(int, input().split()))

min_houses = 1
max_houses = 1

for i in range(1, n):
    if x[i] != x[i - 1]:
        min_houses += 1
    if x[i] != x[i - 1] and x[i] != x[i - 1] + 1:
        max_houses += 1

print(min_houses, max_houses)
