
import sys

def read_int():
    return int(sys.stdin.readline())

def read_line():
    return sys.stdin.readline().strip()

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def solve():
    s = read_line() # string
    b = read_ints() # list of ints
    t = ['a'] * len(s) # list of chars
    for i in range(len(s)-1, -1, -1):
        t[i] = chr(ord(s[i])+b[i])
    return ''.join(t)

def main():
    print(solve())

if __name__ == '__main__':
    main()
