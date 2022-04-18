# https://codeforces.com/problemset/problem/1385/A

n = int(input())
a = list(map(int, input().split()))

disturbed = set()

for i in range(1, n - 1):
    if a[i - 1] == a[i + 1] == 1 and a[i] == 0:
        disturbed.add(a[i - 1])
        disturbed.add(a[i + 1])

print(len(disturbed))
