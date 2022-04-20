

import sys

def main():
    input = sys.stdin.readline
    P,Q,R = map(int, input().split())
    min_time = min(P+Q, P+R, Q+R)
    print(min_time)

if __name__ == '__main__':
    main()