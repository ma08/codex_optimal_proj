

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = [0] * n
for i in range(n):
    c[(a[i] + b[i]) % n] += 1

for i in range(n):
    for j in range(c[i]):


def func(n):
    if n == 1:
        return 1
    else:
        return func(n - 1) + 1


n = int(input())
print(func(n))
        print(i, end=" ")
