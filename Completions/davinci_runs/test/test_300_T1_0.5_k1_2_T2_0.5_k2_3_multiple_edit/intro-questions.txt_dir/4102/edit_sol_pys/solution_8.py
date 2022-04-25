#!/usr/bin/env python3

import sys

def is_lucky_number(number):
    if len(number) == 1:
        return True
    else:
        return False

def main():
    number = sys.stdin.readline().strip()
    if is_lucky_number(number):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
