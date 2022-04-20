
#
#-----Solution-----

n, m = map(int, input().split())
a = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(i, n):
        if (j - i + 1) % 2 == 1:
            if a[(j + i) // 2] == m:
                count += 1
        else:
            if a[(j + i) // 2] == m or a[(j + i) // 2 + 1] == m:
                count += 1

print(count)
