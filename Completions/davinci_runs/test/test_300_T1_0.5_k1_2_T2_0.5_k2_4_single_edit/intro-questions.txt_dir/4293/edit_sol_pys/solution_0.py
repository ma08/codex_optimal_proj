import sys
input = sys.stdin.readline


def main():
    P, Q, R = map(int, input().split())
    print(min(P+Q, Q+R, R+P))

if __name__ == '__main__':
    main()
