

def max_adj_diff(n, m):
    if n == 1:
        return 0
    return m - 1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        print(max_adj_diff(n, m))