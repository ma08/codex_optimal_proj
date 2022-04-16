

def solve(n, m, a, l, r):
    print "Hello world!"

if __name__ == '__main__':
    n, m = [int(i) for i in raw_input().split()]
    a = [int(i) for i in raw_input().split()]
    l = [int(raw_input().split()[0]) for i in range(m)]
    r = [int(raw_input().split()[1]) for i in range(m)]
    solve(n, m, a, l, r)
