

def solve(n, m, a, l, r):
    for i in range(m):
        print(sum(a[l[i]-1:r[i]]))
    return

if __name__ == '__main__':
    n, m = [int(i) for i in raw_input().split()]
    a = [int(i) for i in raw_input().split()]
    l = []
    r = []
    for i in range(m):
        l.append(int(raw_input().split()[0]))
        r.append(int(raw_input().split()[1]))

    solve(n, m, a, l, r)
