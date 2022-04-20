

n = int(input())
x = list(map(int, input().split()))

min_houses = max(x) - min(x)
max_houses = n - 1

for i in range(n):
    if x[i] == 1 or x[i] == n:
        max_houses -= 2

print(min_houses + 1, max_houses)
