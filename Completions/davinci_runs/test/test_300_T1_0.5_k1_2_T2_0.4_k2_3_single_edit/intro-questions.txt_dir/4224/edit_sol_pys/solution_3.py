

N = int(input())
a = [int(x) for x in input().split()][:N]

count = 0

for i in range(N):
    while a[i] % 2 == 0:
        a[i] /= 2
        count += 1

print(count)
