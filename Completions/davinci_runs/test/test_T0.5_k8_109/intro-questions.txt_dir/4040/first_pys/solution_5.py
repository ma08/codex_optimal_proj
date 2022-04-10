

import sys

def main():
  lines = [line.strip() for line in sys.stdin]
  n, m, d = [int(x) for x in lines[0].split()]
  c = [int(x) for x in lines[1].split()]
  if (sum(c) > n):
    print('NO')
    return
  for i in range(1, m):
    if (c[i] > d):
      print('NO')
      return
  a = [0 for x in range(n)]
  for i in range(m):
    j = 0
    while (c[i] > 0):
      a[j] = i + 1
      c[i] -= 1
      j += 1
  print('YES')
  print(' '.join([str(x) for x in a]))

if __name__ == '__main__':
  main()