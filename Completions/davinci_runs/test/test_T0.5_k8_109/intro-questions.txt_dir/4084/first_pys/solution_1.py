

N, A, B = list(map(int, input().split()))

def gcd(a, b):
  if a < b:
    a, b = b, a
  if b == 0:
    return a
  return gcd(b, a % b)

def lcm(a, b):
  return (a * b) // gcd(a, b)

def solve(N, A, B):
  l = lcm(A, B)
  blue_num = (N // l) * (A // gcd(A, B))
  rest = (N % l)
  blue_num += min(rest // A, A // gcd(A, B))

  return blue_num

print(solve(N, A, B))