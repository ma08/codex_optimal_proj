#!/usr/bin/env python3


def main():
    # Get input
    x = int(input())
    a = int(input())
    b = int(input())
    # Calculate
    remainder = x - a
    remainder = remainder - (remainder // b) * b
    # Print
    print(remainder)


if __name__ == '__main__':
    main()
