import sys

a, b, c = map(int, input().split())

print(a + b + c - max(a, b, c) - min(a, b, c))  # 中央値を求める
