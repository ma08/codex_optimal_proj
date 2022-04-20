
n = int(input())
a = [int(i) for i in input().split()]

max_diff = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        max_diff = max(max_diff, abs(a[i] - a[j]))

print(max_diff)
