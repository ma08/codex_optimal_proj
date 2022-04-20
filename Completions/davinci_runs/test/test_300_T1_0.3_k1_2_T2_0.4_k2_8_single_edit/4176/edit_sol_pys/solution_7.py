
import sys

def main():
    line = sys.stdin.readline().rstrip().split()
    print(lcm(int(line[0]), int(line[1])))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

if __name__ == '__main__':
    main()
