
def solve(n, m, c, b, a):
    count = 0
    for i in range(n):
        if a[i][0] * b[0] + a[i][1] * b[1] + a[i][2] * b[2] + c > 0:
            count += 1
    return count

if __name__ == '__main__':
    n, m, c = map(int, input().split())
    b = map(int, input().split())
    a = []
    for i in range(n):
        a.append(map(int, input().split()))
    print solve(n, m, c, b, a)
