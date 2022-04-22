import random
import sys


def rando(a):
  return random.randint(0, a)

def main():
  x = int(sys.stdin.readline())
  y = int(sys.stdin.readline())

  num = rando(y)
  while True:
    num += 1
    if num % x == 0:
      if num % y == 0:
        print(num)
        break

if __name__ == '__main__':
  main()
