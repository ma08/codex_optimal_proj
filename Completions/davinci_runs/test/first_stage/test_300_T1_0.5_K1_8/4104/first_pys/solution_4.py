

import sys

def main():
    s = sys.stdin.readline().strip()
    s = s.split('+')
    s = [int(x) for x in s]
    s = sum(s)
    print(s)

if __name__ == '__main__':
    main()