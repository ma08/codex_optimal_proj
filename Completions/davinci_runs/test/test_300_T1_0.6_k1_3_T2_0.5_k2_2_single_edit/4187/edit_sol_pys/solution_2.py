
n = int(input())
a = list(map(int, input().split()))
i, j, m = 0, 0, 0
while i < n:
    while j < n and a[j] == 1:
        j += 1
    m = max(m, j - i)
    i = j + 1
    j = i
print(m)
