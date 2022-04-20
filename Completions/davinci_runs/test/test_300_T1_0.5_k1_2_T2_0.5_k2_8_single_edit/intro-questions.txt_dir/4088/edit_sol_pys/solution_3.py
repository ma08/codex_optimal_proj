

import sys

def read_int():
    return int(sys.stdin.readline())

def read_line():
    return sys.stdin.readline().strip()

def read_ints():
    return list(map(int, sys.stdin.readline().split()))
def read_lines(n):
    return [read_line() for _ in range(n)]

def read_matrix(n):
    return [read_ints() for _ in range(n)]


def solve():
    s = read_line()
    m = read_int()
    b = read_ints()
    t = ['a'] * len(s)
    for i in range(len(s)-1, -1, -1):
        t[i] = chr(ord(s[i])+b[i])
    return ''.join(t)

def main():
    q = read_int()
    for _ in range(q):
        print(solve())

if __name__ == '__main__':
    main()
