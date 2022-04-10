n = int(input())
a = list(map(int, input().split()))
total = sum(a)

count = 0
for i in range(n):
    if a[i] == total-a[i]:
        count += 1
        print(i+1, end=' ')
if not count:
    print(-1)
