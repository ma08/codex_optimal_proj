

n = int(input())

a = list(map(int, input().split()))

s = 0

c = 0

for i in range(1, n):

    if s + a[i] == 0:
        c += 1

        s = a[i]

print(c)
