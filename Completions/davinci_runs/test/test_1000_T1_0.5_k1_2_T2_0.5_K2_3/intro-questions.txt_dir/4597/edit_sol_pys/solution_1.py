import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    n = int(input())

    print(factorial(n))

if __name__ == '__main__':
    main()
