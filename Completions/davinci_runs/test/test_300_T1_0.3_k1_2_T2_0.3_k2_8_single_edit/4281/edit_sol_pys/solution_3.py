
n = int(input())
x = list(map(int, input().split()))

min_houses = max(x) - min(x)
max_houses = n - 1

for i in range(n):
    if x[i] == min(x) or x[i] == max(x):
        max_houses -= 2

print(min_houses, max_houses)
