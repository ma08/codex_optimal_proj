

def solve(n, m, a, l, r, p):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    print n, m, a, l, r, p

if __name__ == '__main__':
    n, m = [int(i) for i in raw_input().split()]
    a = [int(i) for i in raw_input().split()]
    l = []
    p = []
    r = []
    for i in range(m):
        l.append(int(raw_input().split()[0])-1)
        r.append(int(raw_input().split()[1])-1)
        p.append(int(raw_input().split()[2]))
    solve(n, m, a, l, r, p)
