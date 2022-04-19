

import sys, math

def main():
  n = int(sys.stdin.readline().strip())
  for i in range(n):
    num = int(sys.stdin.readline().strip())
    print(math.factorial(num))

if __name__ == '__main__':
  main()
