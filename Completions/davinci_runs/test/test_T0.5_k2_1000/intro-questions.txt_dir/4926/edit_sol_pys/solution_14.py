import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def euler(n):
    e = 0
    for i in range(0, n + 1):
        e += 1 / factorial(i)
    return e

def main():
    n = int(sys.stdin.readline().strip())
    print(euler(n))

if __name__ == '__main__':
    main()
