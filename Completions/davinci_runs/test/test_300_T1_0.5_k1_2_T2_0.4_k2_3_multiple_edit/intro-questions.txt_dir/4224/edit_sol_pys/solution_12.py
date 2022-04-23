
import sys

# input
N = int(input())
A = int(input())
B = int(input())
C = int(input())
X = int(input())

# solve
ans = 0  # 合計金額が500円のものの枚数
for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            total = 500 * i + 100 * j + 50 * k
            if total == X:
                ans += 1

print(ans)
