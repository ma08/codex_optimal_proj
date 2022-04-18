
import sys

def read_int():
    return int(sys.stdin.readline())

def read_line():
    return sys.stdin.readline().strip()

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def solve():
    s = read_line()
    m = read_int()
    b = read_ints()
    t = ['a'] * (len(s) + 1)
    for i in range(len(s)-1, -1, -1):
        t[i] = chr(ord(s[i]) + b[i])
    return ''.join(t)

def main():
    q = read_int()
    for _ in range(q):
        print(solve())

if __name__ == '__main__':
    main()
