
import sys

def read_ints():
    return [int(x) for x in sys.stdin.readline().split()]

def solve(n, a):
    print(n, a)

if __name__ == "__main__":
    m, n = read_ints()
    t = read_ints()
    x = read_ints()
    solve(m, n, t, x)
