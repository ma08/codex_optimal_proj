

n = int(input())
a = list(map(int, input().split()))

i = 0
j = 0

while i < n and j < n:
    if a[j] == 0:
        j += 1
    else:
        j += 1
        if a[j % n] == 0:
            j += 1

print(j - i - 1)