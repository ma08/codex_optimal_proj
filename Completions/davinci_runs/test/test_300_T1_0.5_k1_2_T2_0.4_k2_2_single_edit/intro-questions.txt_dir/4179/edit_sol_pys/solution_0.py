

def solve(n, m, c, b, a, k):
    # Write your code here
    # To print results to the standard output you can use print
    # print a[0][0]
    # print b[0]
    # print a[0][0] * b[0]
    # Example: print "Hello world!"
    count = 0
    for i in range(n):
        if a[i][0] * b[0] + a[i][1] * b[1] + a[i][2] * b[2] + c > k:
            count += 1
    return count

if __name__ == '__main__':
    n, m, c, k = map(int, raw_input().split())
    b = map(int, raw_input().split())
    a = []
    for i in range(n):
        a.append(map(int, raw_input().split()))
    print solve(n, m, c, b, a, k)
