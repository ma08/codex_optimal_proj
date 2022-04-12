
import sys

def main():
    a, b, c = map(int, sys.stdin.readline().split(' '))
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    if c - b == b - a:
        print(c + b - a)
    elif c - a == b - a:
        print(c - a + b)
    else:
        print(a + b - c)

if __name__ == '__main__':
    main()
