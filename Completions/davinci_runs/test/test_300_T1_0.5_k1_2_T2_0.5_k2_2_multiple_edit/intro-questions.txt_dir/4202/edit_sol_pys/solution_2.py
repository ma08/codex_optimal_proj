import sys


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 全部のループを回す
    for i in range(M):
        B, C = map(int, input().split())
        # B回ループ
        for j in range(B):
            # Aの中のCより小さいものをCにする
            if A[j] < C:
                A[j] = C
            else:
                break
    print(sum(A))


if __name__ == '__main__':
    main()
