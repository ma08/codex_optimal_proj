
n = int(input())
P = [int(x) for x in input().split()]

count = 0
for i in range(1, n - 1):
    if P[i - 1] < P[i] < P[i + 1] or P[i + 1] < P[i] < P[i - 1]:
        count += 1

print(count)
