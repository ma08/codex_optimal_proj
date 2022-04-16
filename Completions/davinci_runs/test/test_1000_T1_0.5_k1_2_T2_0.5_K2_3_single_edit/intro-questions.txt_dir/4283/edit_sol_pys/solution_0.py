

n = int(input())
a = list(map(int, input().split()))
a.sort()
count = 0
if n == 1:
    print(1)
    exit(0)

i = 0
j = 1

while j < n:
    if a[j] - a[i] <= 5:
        j += 1
    else:
        i = j
        j += 1
    count = max(count, j - i)

print(count)
