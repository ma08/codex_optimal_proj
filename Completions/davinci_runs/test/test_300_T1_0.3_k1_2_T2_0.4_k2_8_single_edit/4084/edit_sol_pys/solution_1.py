
import sys

def main():
    n, a, b = map(int, sys.stdin.readline().split())
    print(n // (a + b) * a + min(n % (a + b), a)) 

if __name__ == '__main__':
    main()
