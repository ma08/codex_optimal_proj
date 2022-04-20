#!/usr/bin/env python3

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [(x + y) % n for (x, y) in zip(a, b)]
    c.sort()
    print(' '.join([str(x) for x in c]))

if __name__ == '__main__':
    main()
