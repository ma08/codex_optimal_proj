

def main():
    N = int(input())  # 1行目
    A, B, C, D, E = list(map(int, input().split()))  # 2行目

    ans = 0

    for n in range(N):
        d = n // (A + B)  # 所要時間
        e = d // (C + D)  # 待ち時間
        ans = max(ans, n + d + e)

    print(ans)

if __name__ == "__main__":
    main()
