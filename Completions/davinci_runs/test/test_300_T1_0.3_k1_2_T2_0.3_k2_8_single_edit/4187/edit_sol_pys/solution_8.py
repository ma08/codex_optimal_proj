
n = int(input())
a = [int(i) for i in input().split()]

max_rest = 0
rest = 0

for i in range(n):
    if a[i] == 1:
        rest += 1
    else:
        max_rest = max(max_rest, rest)
        rest = 0

max_rest = max(max_rest, rest)

print(max_rest)
