

import sys

def multigram(s):
    if len(s) % 2 == 0:
        half = len(s)//2
        first = s[:half]
        second = s[half:]
        if first == second:
            return first
    return -1

def main():
    s = sys.stdin.readline().strip()
    print(multigram(s))

if __name__ == "__main__":
    main()
