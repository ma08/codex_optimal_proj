

def solve(n, m, k, grid):
  # TODO: Solve the problem!
  return 0

import sys

def main():
  n, m, k = map(int, sys.stdin.readline().split())
  grid = []
  for i in range(n):
    row = map(int, sys.stdin.readline().split())
    grid.append(row)
  print solve(n, m, k, grid)

if __name__ == '__main__':
  main()