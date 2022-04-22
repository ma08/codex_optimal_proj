

N = int(input())
a = [int(x) for x in input().split()]

count = 0

for i in range(N):
    i = a[i]
    while i % 2 == 0:
        i /= 2
        count += 1

print(count)
