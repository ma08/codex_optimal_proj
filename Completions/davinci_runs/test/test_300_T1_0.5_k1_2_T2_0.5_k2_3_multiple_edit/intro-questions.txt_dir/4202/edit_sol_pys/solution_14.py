import sys
sys.setrecursionlimit(1000000)

import math

def check_prime(n):
  if n == 1: return False

  for k in range(2, int(math.sqrt(n)) + 1):
    if n % k == 0:
      return False
  
  return True

def main():
  N = int(input())
  if check_prime(N):
    print("YES")
  else:
    print("NO")

main()

L, R = map(int, input().split())
if R - L > 2019:
    print(0)
else:
    a = L % 2019
    b = R % 2019
    if a < b:
        a, b = b, a
    min_val = 2019
    for i in range(b+1, a):
        for j in range(i+1, a+1):
            min_val = min(min_val, i * j % 2019)
    print(min_val)
