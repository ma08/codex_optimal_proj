

def solve(n, m, a, l, r, k):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    pass

if __name__ == '__main__':
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    l = []
    k = []
    r = []
    for i in range(m):
        l.append(int(input().split()[0]))
        r.append(int(input().split()[1]))
        k.append(int(input().split()[2]))
    solve(n, m, a, l, r, k)
