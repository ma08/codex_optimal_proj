

def main():
    n, r = map(int, input().split())
    a, b = [0] * n, [0] * n  # a:時間, b:攻撃力
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    if solve(n, r, a, b):
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
