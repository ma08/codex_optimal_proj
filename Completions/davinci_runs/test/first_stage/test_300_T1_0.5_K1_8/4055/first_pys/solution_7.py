

n = int(input())
a = [int(i) for i in input().split()]

disturbed = 0
for i in range(1, n - 1):
    if (a[i - 1] == 1 and a[i + 1] == 1 and a[i] == 0):
        disturbed += 1

print(disturbed)