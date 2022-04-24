

class Solution:
    def __init__(self):
        self.N = int(input())
        self.A = [int(x) for x in input().split()]

    def solve(self):
        n = self.N
        a = self.A
        dp_l = [0] * n
        dp_r = [0] * n
        dp_l[0] = 1
        dp_r[n - 1] = 1
        for i in range(1, n):
            if a[i] > a[i - 1]:
                dp_l[i] = dp_l[i - 1] + 1
            else:
                dp_l[i] = 1
        for i in range(n - 2, -1, -1):
            if a[i] < a[i + 1]:
                dp_r[i] = dp_r[i + 1] + 1
            else:
                dp_r[i] = 1
        print(max([dp_l[i] + dp_r[i] - 1 for i in range(n)]))

    def solve2(self):
        n = self.N
        a = self.A
        dp_l = [0] * n
        dp_r = [0] * n
        dp_l[0] = 1
        dp_r[n - 1] = 1
        for i in range(1, n):
            if a[i] > a[i - 1]:
                dp_l[i] = dp_l[i - 1] + 1
            else:
                dp_l[i] = 1
        for i in range(n - 2, -1, -1):
            if a[i] < a[i + 1]:
                dp_r[i] = dp_r[i + 1] + 1
            else:
                dp_r[i] = 1
        l, r = 0, 0
        ans = 0
        for i in range(n):
            if dp_l[i] + dp_r[i] - 1 > ans:
                ans = dp_l[i] + dp_r[i] - 1
                l = i
                r = i
        print(ans)
        ans = ""
        for i in range(l):
            ans += 'L'
        for i in range(r + 1, n):
            ans += 'R'
        print(ans)

    def solve3(self):
        n = self.N
        a = self.A
        dp_l = [0] * n
        dp_r = [0] * n
        dp_l[0] = 1
        dp_r[n - 1] = 1
        for i in range(1, n):
            if a[i] > a[i - 1]:
                dp_l[i] = dp_l[i - 1] + 1
            else:
                dp_l[i] = 1
        for i in range(n - 2, -1, -1):
            if a[i] < a[i + 1]:
                dp_r[i] = dp_r[i + 1] + 1
            else:
                dp_r[i] = 1
        l, r = 0, 0
        ans = 0
        for i in range(n):
            if dp_l[i] + dp_r[i] - 1 > ans:
                ans = dp_l[i] + dp_r[i] - 1
                l = i
                r = i
        print(ans)
        ans = ""
        for i in range(l):
            ans += 'L'
        for i in range(r + 1, n):
            ans += 'R'
        print(ans)
