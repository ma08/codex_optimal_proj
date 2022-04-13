
import sys

def main():
    n = int(sys.stdin.readline())
    if n < 1 or n > 100:
        return
    for i in range(n):
        a, b = [int(x) for x in sys.stdin.readline().split()]
        if a < 1 or a > 100 or b < 1 or b > 100:
            return
        else:
            print(a * b)

if __name__ == '__main__':
    print(main())
