

def solve(n, m, a, t):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    pass

if __name__ == '__main__':
    n, m = [int(i) for i in raw_input().split()]
    a = [int(i) for i in raw_input().split()]
    t = []
    for i in range(m):
        t.append(int(raw_input().split()))
    solve(n, m, a, t)
