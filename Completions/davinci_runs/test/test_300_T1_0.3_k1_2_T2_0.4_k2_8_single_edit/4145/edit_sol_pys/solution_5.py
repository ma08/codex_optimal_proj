
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
    x = int(input())
    while True:
        if isPrime(x):
            print(x)
            return
        x += 1

if __name__ == '__main__':
    main()
