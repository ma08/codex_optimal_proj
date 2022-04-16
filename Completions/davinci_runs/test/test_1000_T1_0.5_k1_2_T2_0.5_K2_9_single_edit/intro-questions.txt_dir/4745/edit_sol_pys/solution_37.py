

# SOLUTION
n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pages = 0
i = 0
j = 0
while i < n and j < m:
    if a[i] + b[j] <= k:
        i += 1
        j += 1
        pages += 1
    elif a[i] > k:
        break
    elif a[i] + b[j] > k:
        j += 1

print(pages)
