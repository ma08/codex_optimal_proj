#!/usr/bin/env python3


def main():
    A, B, T = map(int, input().split())
    print(B * (T // A + 1))


if __name__ == '__main__':
    main()
