
n = int(input())
a = list(map(int, input().split()))
a.sort()

i = 0
j = 1

count = 0
while j < n:
    if a[j] - a[i] <= 5:
        j += 1
    else:
        i = j
        j += 1
    count = max(count, j - i)

print(count)
