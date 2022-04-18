

import sys

def main():
    s = sys.stdin.readline()
    print(max(s.count('R'), s.count('RR')))

if __name__ == '__main__':
    main()
