

n = int(input())
a = list(map(int, input().split()))
max_length = [0] * n

for i in range(1, n):
    if a[i] <= 2 * a[i - 1]:
        max_length[i] = max_length[i - 1] + 1
    else:
        max_length[i] = max_length[i - 1]

print(max_length[-1] + 1)
