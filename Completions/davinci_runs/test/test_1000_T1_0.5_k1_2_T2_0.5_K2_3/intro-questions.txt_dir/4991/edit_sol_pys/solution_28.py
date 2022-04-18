import sys

def f(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + f(n/2)
    else:
        return n + f((3*n) + 1)

def main():
    num = int(sys.stdin.readline().strip())
    print(f(num))

if __name__ == '__main__':
    main()
