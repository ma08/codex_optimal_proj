


def main():
    N = int(input())
    S = input()
    T = input()

    ans = 0
    for i in range(N):
        if S[i] != T[i]:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()

def main():
    A, B, C = map(int, input().split())
    I, J, K = map(int, input().split())

    min_cocktail = min(A / I, B / J, C / K)  # 最少で作れるカクテル

    print(max(A - I * min_cocktail, 0), max(B - J * min_cocktail, 0), max(C - K * min_cocktail, 0))


if __name__ == "__main__":
    main()
