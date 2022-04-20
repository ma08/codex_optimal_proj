
import sys

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def main():
    data = sys.stdin.read().split()
    for i in range(len(data)):
        if isPrime(int(data[i])):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()