import sys
import math



def main():
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b:
        print(c)
    elif a == c:
        print(b)
    else:
        print(a)


if __name__ == "__main__":
    main()
