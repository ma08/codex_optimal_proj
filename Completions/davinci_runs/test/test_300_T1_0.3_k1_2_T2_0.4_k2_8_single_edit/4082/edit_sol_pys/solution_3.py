

def solve(n, m, a, b):
    pass

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:m]
    print(solve(n, m, a, b))
