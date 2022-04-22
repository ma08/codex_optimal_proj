


def main():
    N = int(input())  # 列数
    M = int(input())  # 行数
    C = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    B = list(map(int, input().split()))
    ans = []
    for i in range(M):
        temp = 0
        for j in range(N):
            temp += A[j][i] * B[j]
        ans.append(temp + C[i])
    for k in range(M):
        print(ans[k])


if __name__ == '__main__':
    main()
