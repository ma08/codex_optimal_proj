

def solve(n, m, a, l, r, q):
    print(n)
    print(m)
    print(a)
    print(l)
    print(r)
    print(q)

if __name__ == '__main__':
    n, m = [int(i) for i in raw_input().split()]
    a = [int(i) for i in raw_input().split()]
    l = [0]
    r = [0]
    q = [0]
    for i in range(m):
        l[i] = int(raw_input().split()[0])
        r[i] = int(raw_input().split()[1])
        q[i] = int(raw_input().split()[2])
    solve(n, m, a, l, r, q)
