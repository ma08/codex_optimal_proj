
# https://atcoder.jp/contests/abc081/tasks/abc081_a
# Read input
k, x = map(int, input().split())

# Check if the coins add up to X yen or more, print the result
print('Yes' if k * 500 >= x else 'No')
