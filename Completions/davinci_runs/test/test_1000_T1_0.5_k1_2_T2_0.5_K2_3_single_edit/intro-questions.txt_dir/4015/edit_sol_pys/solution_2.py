import sys




def main():
    # 計算量O(n)
    n = int(input())
    a = list(map(int, input().split()))
    # 二分探索で求めたいindexを求める
    # 累積和を作る
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    # print(s)
    q = int(input())
    m = list(map(int, input().split()))
    for x in m:
        # 二分探索で求める
        # l = 0
        # r = n
        # ここでは二分探索の計算量がO(logN)
        # while r - l > 1:
        #     i = (r + l) // 2
        #     if s[i] >= x:
        #         r = i
        #     else:
        #         l = i
        # print(r)
        # 二分探索の計算量をO(N)に落とす
        for i in range(n):
            if s[i] >= x:
                print(i)
                break


if __name__ == '__main__':
    main()
