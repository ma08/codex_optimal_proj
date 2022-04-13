# coding: utf-8
import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    s = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
    s.sort(reverse=True)
    if s[0] + s[1] + s[2] < 10:
        print(s[0] + s[1] + s[2])

if __name__ == '__main__':
    main()
