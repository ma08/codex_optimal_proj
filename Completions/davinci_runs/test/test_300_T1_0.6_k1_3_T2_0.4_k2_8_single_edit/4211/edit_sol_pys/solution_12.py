

def main():
    N = int(input())
    B = [int(i) for i in input().split()]
    A = [0] * N
    A[0] = B[0]  # 一番目はそのまま
    for i in range(1, N - 1):  # 二番目からN-2番目
        A[i] = min(B[i - 1], B[i])  # 左右のうち小さい方を代入
    A[N - 1] = B[N - 2]  # 最後は左側の値を代入
    print(sum(A))

if __name__ == '__main__':
    main()
