


def f():
    n = int(input())
    a = list(input())
    f = list(map(int, input().split()))
    f_dict = {}
    for i in range(1, 10):
        f_dict[i] = f[i - 1]
    for i in range(n):
        a[i] = f_dict[int(a[i])]
    a = ''.join(a)
    print(a)


f()