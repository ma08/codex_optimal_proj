
a = int(input().split()[0])
b = int(input().split()[0])
c = int(input().split()[0])
x = int(input().split()[0])


def f(a, b, c, x):
    return 500 * a + 100 * b + 50 * c


ans = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if f(i, j, k, x) == x:
                ans += 1

print(ans)
