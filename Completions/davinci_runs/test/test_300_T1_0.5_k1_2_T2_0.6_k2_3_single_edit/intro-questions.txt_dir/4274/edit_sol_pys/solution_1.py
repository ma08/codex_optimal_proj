# https://atcoder.jp/contests/abc097/tasks/abc097_a


N, M = map(int, input().split())

if abs(N - M) <= 1:
    print("Yes")
else:
    print("No")
