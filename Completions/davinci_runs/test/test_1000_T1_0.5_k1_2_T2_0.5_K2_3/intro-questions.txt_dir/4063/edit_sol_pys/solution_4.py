
n = int(input())
a = list(map(int, input().split()))

a.sort()

cnt = 0
for i in range(n//2+1):
    if a[i] == a[n-i-1]:
        cnt += 1
    else:
        break
print(n//2 + cnt)
