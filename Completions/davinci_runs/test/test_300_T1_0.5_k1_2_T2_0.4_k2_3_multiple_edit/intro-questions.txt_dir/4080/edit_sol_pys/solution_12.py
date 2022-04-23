

def solve(n, m, a, l, r, k, d):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    for i in range(m):
        for j in range(l[i], r[i]):
            a[j] += k[i]
    for i in range(n):
        if a[i] > d:
            return "NO"
    return "YES"

if __name__ == '__main__':
    n, m = [int(i) for i in raw_input().split()]
    a = [int(i) for i in raw_input().split()]
    l = []
    k = []
    d = int(raw_input())
    r = []
    for i in range(m):
        l.append(int(raw_input().split()[0]))
        r.append(int(raw_input().split()[1]))
        k.append(int(raw_input().split()[2]))
    print solve(n, m, a, l, r, k, d)
