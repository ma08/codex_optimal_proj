import sys
import math



def read_int():
    return int(sys.stdin.readline())

def read_line():
    return sys.stdin.readline().strip()

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def solve(s, m, b):
    t = [''] * (len(s) + m)
    for i in range(len(s)):
        t[i] = chr(ord(s[i]) + b[i])
    for i in range(len(s), len(s) + m):
        t[i] = chr(ord('a') + b[i])
    return ''.join(t[::-1])

def main():
    q = read_int()
    for _ in range(q):
        print(solve())

if __name__ == '__main__':
    main()
