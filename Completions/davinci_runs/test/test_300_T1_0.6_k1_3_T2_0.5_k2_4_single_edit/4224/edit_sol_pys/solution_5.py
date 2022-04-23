
N = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(N):
    if a[i] % 2 == 0 and a[i] % 3 != 0 and a[i] % 5 != 0:
        count += 1

print(count)
