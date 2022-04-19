

def main():
    n = int(input())  # 入力値
    A = [int(i) for i in input().split()]  # 入力値をリストに変換
    D = min(A)  # 最小値
    for i in range(n):  # 全ての要素から最小値を引く
        A[i] = A[i] - D  # 全ての要素から最小値を引く
    if sum(A) % n == 0:  # 全ての要素の合計がnで割り切れるならば
        print(D)
    else:  # 全ての要素の合計がnで割り切れないならば
        print(-1)

if __name__ == "__main__":
    main()
