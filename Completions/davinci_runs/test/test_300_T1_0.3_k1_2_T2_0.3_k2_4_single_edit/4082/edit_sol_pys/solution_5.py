

def solve(n, m, a):
    pass

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    print(solve(n, m, a))
