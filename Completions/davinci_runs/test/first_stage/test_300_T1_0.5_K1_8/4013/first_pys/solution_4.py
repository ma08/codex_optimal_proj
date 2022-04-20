

def solve(n, a):
    a.sort()
    if n == 2:
        return a[1] - a[0]
    return min(a[1] - a[0], a[n - 1] - a[n - 2])

if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    print(solve(n, a))