

import sys

def main():
  n = int(sys.stdin.readline())
  num = n
  while num > 0:
    if num % 2 == 0:
      print(num) 
      exit()
    num += n

if __name__ == '__main__':
  main()
