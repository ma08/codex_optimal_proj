
# test
import sys

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def euler_approx(n):
    e = 0
    for i in range(n+1):
        e += 1/factorial(i)
    return e

def main():
    n = int(sys.stdin.readline())
    print(euler_approx(n))

if __name__ == '__main__':
    main()
