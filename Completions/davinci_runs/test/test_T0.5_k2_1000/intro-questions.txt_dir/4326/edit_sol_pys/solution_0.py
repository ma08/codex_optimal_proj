
# https://atcoder.jp/contests/abc071/tasks/arc081_a
n = int(input())

if n % 3 == 0:
    print(n // 3 * 2)
elif n % 3 == 1:
    print((n - 4) // 3 * 2 + 1)
else:
    print((n - 2) // 3 * 2 + 1)
