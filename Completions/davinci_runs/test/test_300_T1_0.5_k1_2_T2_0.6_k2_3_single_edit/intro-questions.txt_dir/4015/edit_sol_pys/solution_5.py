def get_input():
    n, m = map(int, input().split())
    return n, m

def solve(n, m):
    if n == m:
        return 0
    if n > m:
        return -1
    if m % n != 0:
        return -1
    return solve(n * 2, m) + 1 if m % (n * 2) == 0 else solve(n * 3, m) + 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve(n, m))
