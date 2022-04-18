

def solve(n, m, a, l, r, d):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    print(n, m, a, l, r, d)

if __name__ == '__main__':
    n, m = [int(i) for i in raw_input().split()]
    a = [int(i) for i in raw_input().split()]
    l = []
    d = []
    r = []
    for i in range(m):
        l.append(int(raw_input().split()[0]))
        r.append(int(raw_input().split()[1]))
        d.append(raw_input().split()[2])
    solve(n, m, a, l, r, d)
