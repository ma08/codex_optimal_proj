import sys
import math



def solve(line):
    return line * (line - 3) // 2


def main():
    n = int(sys.stdin.readline())
    print(solve(n))

if __name__ == '__main__':
    main()
