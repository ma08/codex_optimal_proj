
def f(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
n = int(input())
p = []
for i in range(n):
    p.append([int(x) for x in input().split()])
if n == 1:
    print(0)
else:
    print(f(p[0], p[1]))
