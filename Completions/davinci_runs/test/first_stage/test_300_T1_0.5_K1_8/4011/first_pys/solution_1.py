
n = int(input())
a = input()
f = list(map(int, input().split()))

a = list(map(int, a))

def f_a(a, f):
    res = 0
    for i in range(len(a)):
        res = res * 10 + f[a[i] - 1]
    return res

max_f = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        x = a[i:j]
        x = f_a(x, f)
        if x > max_f:
            max_f = x

print(max_f)