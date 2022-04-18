


def solve(n, m, s, d, c, a):
  # Write your code here
  # return a list of length s with your solution or None if impossible
  return [0] * s


n = int(input())
m = int(input())
s = int(input())
d = int(input())
c = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

res = solve(n, m, s, d, c, a)
if res is None: print("impossible")
else: print(" ".join([str(x) for x in res]))
