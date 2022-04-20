

N = int(input())

"""
A \times B + C = N
A \times B = N - C

N - C \geq 1
N - C \leq N

1 \leq C \leq N
"""

ans = 0
for c in range(1, N + 1):
    ans += N // c
print(ans)