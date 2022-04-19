#!/usr/bin/env python3



def main():
    n = int(input())
    a = [int(s) for s in input().split()]
    print(n)
    print(' '.join(map(str, a)))

if __name__ == "__main__":
    main()
