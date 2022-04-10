

# n = int(input())
# a = list(map(int, input().split()))

n = 10
a = [1, 1, 0, 1, 1, 0, 1, 0, 1, 0]

k = 0
for i in range(1, n - 1):
    if a[i - 1] == 1 and a[i + 1] == 1 and a[i] == 0:
        a[i] = 1
        k += 1
print(k)