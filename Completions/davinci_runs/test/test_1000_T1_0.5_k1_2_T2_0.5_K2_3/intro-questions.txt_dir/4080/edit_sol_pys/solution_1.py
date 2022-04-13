

def solve(n, m, a, t, p):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    pass

if __name__ == '__main__':
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    t = [0] * m
    for i in range(m):
        t[i] = [int(j) for j in input().split()]
    p = [int(i) for i in input().split()]
    solve(n, m, a, t, p)
