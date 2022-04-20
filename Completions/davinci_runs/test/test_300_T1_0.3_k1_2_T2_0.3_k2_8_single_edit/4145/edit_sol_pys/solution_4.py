
import math

def isPrime(num):
  if num == 1:
    return False
  if num == 2:
    return True
  if num % 2 == 0:
    return False
  for i in range(3, int(math.sqrt(num)) + 1, 2):
    if num % i == 0:
      return False
  return True

def main():
  X = int(input())
  while True:
    if isPrime(X):
      print(X)
      return
    X += 1

if __name__ == '__main__':
  main()
