

n = int(input())
a = list(map(int, input().split()))
a.sort()

if n == 1:
    print(1)
    exit()

i = 0
j = 1

count = 0
while j < n:
    if a[j] - a[i] <= 5:
        j += 1
    else:
        i = j
    count = max(count, j - i)

print(count)
