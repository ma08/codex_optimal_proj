
n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

cnt = 0
for i in range(n // 2):
    if a[i] == a[i + n // 2]:
        cnt += 1
    else:
        break
print(n // 2 + cnt)
