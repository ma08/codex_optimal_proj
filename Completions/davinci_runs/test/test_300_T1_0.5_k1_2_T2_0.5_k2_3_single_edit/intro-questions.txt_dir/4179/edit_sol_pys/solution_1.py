

def solve(n, m, c, b, a, k):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    count = 0
    for i in range(k):
        for j in range(n):
            if a[j][0] * b[0] + a[j][1] * b[1] + a[j][2] * b[2] + c > 0:
                count += 1
    return count

if __name__ == '__main__':
    n, m, c = map(int, raw_input().split())
    b = map(int, raw_input().split())
    a = []
    for i in range(n):
        a.append(map(int, raw_input().split()))
    k = int(raw_input())
    print solve(n, m, c, b, a, k)
