

n = int(input())
houses = list(map(int, input().split()))

min_houses = 1
max_houses = 1

for i in range(1, n):
    if houses[i] != houses[i-1]:
        min_houses += 1

if houses[0] == 1:
    min_houses -= 1
if houses[-1] == n:
    min_houses -= 1

for i in range(1, n):
    if houses[i] == houses[i-1]:
        max_houses += 1

print(min_houses, max_houses)