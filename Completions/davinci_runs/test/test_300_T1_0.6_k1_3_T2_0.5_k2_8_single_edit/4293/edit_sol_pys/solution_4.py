
from sys import stdin
readline = stdin.readline

def main():
    P, Q, R = map(int, readline().split())

    print(min(P+Q, Q+R, R+P))

if __name__ == '__main__':
    main()
