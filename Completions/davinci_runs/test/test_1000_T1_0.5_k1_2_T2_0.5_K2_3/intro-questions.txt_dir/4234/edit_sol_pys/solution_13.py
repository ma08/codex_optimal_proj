import sys

def read_string():
    return sys.stdin.readline().strip()

def read_int():
    return int(read_string())

def read_words(sep=' '):
    return read_string().split(sep)

def read_ints(sep=' '):
    return [int(s) for s in read_words(sep)]

def solve():
    n = read_int()
    a = read_ints()
    a.sort()
    print(a[n//2])

if __name__ == '__main__':
    t = read_int()
    for i in range(t):
        solve()
