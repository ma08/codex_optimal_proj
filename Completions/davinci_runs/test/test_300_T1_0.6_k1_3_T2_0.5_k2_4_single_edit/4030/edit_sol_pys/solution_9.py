
import sys

class Solver:
    def __init__(self, n, k, a):
        self.n = n  # 商品の個数
        self.k = k  # 合計金額
        self.a = a  # 商品の値段

    def solve(self):
        a = self.a
        n = self.n
        k = self.k

        # 合計金額が0のときは0を返す
        if k == 0:
            return 0

        # 合計金額が負のときは-1を返す
        if k < 0:
            return -1

        # 商品の値段が0のときは-1を返す
        if a[n - 1] == 0:
            return -1

        # 商品の個数が0のときは-1を返す
        if n == 0:
            return -1

        return max(self.solve(n - 1, k), self.solve(n - 1, k - a[n - 1])) + 1


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    solver = Solver(n, k, a)
    res = solver.solve()
    print(res)
