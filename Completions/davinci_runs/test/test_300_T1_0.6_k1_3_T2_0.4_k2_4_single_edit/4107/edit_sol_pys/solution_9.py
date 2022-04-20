

def solve(n, m, l, r):
    return 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        l_i, r_i = map(int, input().split())
        l.append(l_i)
        r.append(r_i)
    print(solve(n, m, l, r))
