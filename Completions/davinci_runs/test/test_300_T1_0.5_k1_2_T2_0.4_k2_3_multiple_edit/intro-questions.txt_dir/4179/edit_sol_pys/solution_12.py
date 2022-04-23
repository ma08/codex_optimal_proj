

def solve(n, m, c, a, b, k):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    max_count = 0
    count = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] * b[j] - c > 0:
                count += 1
        if count > max_count:
            max_count = count
    return max_count

if __name__ == '__main__':
    n, m, c, k = map(int, raw_input().split())
    b = [int(x) for x in raw_input().split()]
    a = []
    for i in range(n):
        a.append([int(x) for x in raw_input().split()])
    print solve(n, m, c, a, b, k)
