
import sys

def main():
    line = sys.stdin.readline().rstrip()
    n = int(line)
    print(factorial(n))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

if __name__ == '__main__':
    main()
