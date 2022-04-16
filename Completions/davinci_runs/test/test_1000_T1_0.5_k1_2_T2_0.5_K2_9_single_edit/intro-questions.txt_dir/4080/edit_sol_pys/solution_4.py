

def solve(n, m, a, l, r, k):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!
    pass

if __name__ == '__main__':
    n, m = [int(i) for i in raw_input().split()]
    a = [int(i) for i in raw_input().split()]
    l = []
    k = []
    r = []
    for i in range(m):
        l.append(int(raw_input().split()[0]) - 1)
        r.append(int(raw_input().split()[1]) - 1)
        k.append(int(raw_input().split()[2]) - 1)
    solve(n, m, a, l, r, k)
