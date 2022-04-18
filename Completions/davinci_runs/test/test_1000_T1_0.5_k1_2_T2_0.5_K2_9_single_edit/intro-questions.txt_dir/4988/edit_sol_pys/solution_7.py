

import sys

def factorial(n):
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1)) % 10

def main():
    for i in range(int(sys.stdin.readline())):
        print(factorial(int(sys.stdin.readline())))

if __name__ == '__main__':
    main()
