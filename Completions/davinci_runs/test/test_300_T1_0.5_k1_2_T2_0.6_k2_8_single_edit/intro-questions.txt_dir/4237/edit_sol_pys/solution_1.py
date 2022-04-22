import sys
import math



def main():
    a = int(sys.stdin.readline())
    b = math.ceil(a / 5)
    c = a % 5

    if c == 0:
        print(b)
    else:
        print(b + 1)

if __name__ == '__main__':
    main()
