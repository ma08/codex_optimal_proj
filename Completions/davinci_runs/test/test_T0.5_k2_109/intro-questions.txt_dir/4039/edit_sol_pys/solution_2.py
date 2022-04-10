
def main():
    n, r = map(int, input().split())
    s, t = [0] * n, [0] * n  # TODO: リスト内包表記
    for i in range(n):
        s[i], t[i] = map(int, input().split())
    if solve(n, r, s, t):
        print('YES')
    else:
        print('NO')

def solve(n, r, a, b):
    for i in range(n):
        r += b[i]
        if r < a[i]:
            return False
    return True

if __name__ == '__main__':
    main()
