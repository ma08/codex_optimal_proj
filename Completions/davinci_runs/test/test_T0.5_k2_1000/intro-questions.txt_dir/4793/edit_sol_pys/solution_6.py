
import sys

def main():
    a, b, c = map(int, sys.stdin.readline().split())
    if a % b == 0:
        print(a // b, 0)
    elif a % c == 0:
        print(0, a // c)
    elif a % c == b % c:
        print(a // b, (a % b) // c)
    else:
        print("Impossible")

if __name__ == '__main__':
    main()
