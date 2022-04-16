

import sys

def main():
    s = sys.stdin.readline().rstrip()
    print(max(s.count('R'),s.count('RR'),s.count('RRR')))

if __name__ == '__main__':
    main()
