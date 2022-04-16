

def main():
    n, k, x = map(int, input().split())  # n = 4, k = 5, x = 100
    A = list(map(int, input().split()))  # A = [1, 2, 3, 4]
    if x < k:  # x < k ならば -1 を出力
        print(-1)  # -1
    elif k == 1:  # k が 1 ならば A の全要素を足した値を出力
        print(sum(A))  # 10
    elif k == 2:  # k が 2 ならば A の最大値を出力
        print(max(A))  # 4
    elif k == 3:  # k が 3 ならば A の先頭と末尾の要素を足した値と A の中央の要素の最大値を比較して大きい方を出力
        print(max(A[0] + A[-1], max(A[1:n-1])))  # 7
    elif k == 4:  # k が 4 ならば A の先頭と末尾の要素を足した値と A の中央の要素の最大値を比較して大きい方を出力
        print(max(A[0] + A[1] + A[-2] + A[-1], max(A[2:n-2])))  # 10
    elif k == 5:  # k が 5 ならば A の先頭と末尾の要素を足した値と A の中央の要素の最大値を比較して大きい方を出力
        print(max(A[0] + A[1] + A[2] + A[-3] + A[-2] + A[-1], max(A[3:n-3])))  # 14
    else:  # それ以外の場合は A の先頭と末尾の要素を足した値と A の中央の要素の最大値を比較して大きい方を出力
        print(max(A[0] + A[1] + A[2] + A[3] + A[-4] + A[-3] + A[-2] + A[-1], max(A[4:n-4])))  # 14

if __name__ == '__main__':
    main()
