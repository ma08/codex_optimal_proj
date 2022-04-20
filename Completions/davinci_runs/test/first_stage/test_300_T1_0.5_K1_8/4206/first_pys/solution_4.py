

import sys

def main():
    input = sys.stdin.readline
    s = input().strip()
    print(len(s) - 1 - s.count('0') - s.count('5'))

if __name__ == '__main__':
    main()