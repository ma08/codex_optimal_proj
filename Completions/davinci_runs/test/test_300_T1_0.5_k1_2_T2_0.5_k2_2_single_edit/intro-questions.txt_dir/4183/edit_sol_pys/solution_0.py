


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a*b // gcd(a, b)


def main():
    N = int(input())
    T = [int(input()) for _ in range(N)]  # 入力をリストで取得
    ans = 1
    for t in T:
        ans = lcm(ans, t)  # 最小公倍数を計算

    print(ans)

if __name__ == '__main__':
    main()
