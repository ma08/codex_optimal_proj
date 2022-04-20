
n = int(input())
x = list(map(int, input().split()))

min_houses = 0
max_houses = 0

for i in range(n):
    if i == 0 or x[i] != x[i-1]:
        min_houses += 1
    if i == 0 or x[i] != x[i-1] and x[i] != x[i-1] + 1:
        max_houses += 1

print(min_houses, max_houses)
