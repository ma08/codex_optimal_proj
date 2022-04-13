import sys

def main():
    k = int(input())
    n = 1
    while 2 ** n < k:
        n *= 2
    print(n, n)

if __name__ == '__main__':
    main()
