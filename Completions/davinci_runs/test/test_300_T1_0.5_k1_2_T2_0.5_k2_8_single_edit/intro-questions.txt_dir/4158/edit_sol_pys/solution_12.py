
import sys


def show(l):
    for i in l:
        print(i, end=' ')
    print()


def show_dict(d):
    for i, j in d.items():
        print(i, j, end=' ')
    print()


def get_max_seq(l):
    d = {}
    m = 0
    for i in l:
        if i in d:
            continue
        d[i] = 1
        for j in range(32):
            if i + 2**j in d:
                d[i + 2**j] = d[i] + 1
            if i - 2**j in d:
                d[i - 2**j] = d[i] + 1
            m = max(m, d[i])
    return m, d



n = int(input())
l = list(map(int, input().split()))

m, d = get_max_seq(l)

if m == 1:
    show(l)
    sys.exit(0)
ans = []
for i, j in d.items():
    if j == m:
        ans.append(i)
show(ans)
