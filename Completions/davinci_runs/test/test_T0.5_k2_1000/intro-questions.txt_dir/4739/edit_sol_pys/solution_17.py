

# SOLUTION 2
import sys

def read_ints():
    return [int(x) for x in sys.stdin.readline().split()]

def solve(n, k, a):
    a = sorted(a)
    i = 0
    while i < n:
        j = i + 1
        while j < n and a[j] - a[i] <= 5:
            j += 1
        if j - i > k:
            return False
        i = j
    return True

if __name__ == "__main__":
    n, k = read_ints()
    a = read_ints()
    print('YES' if solve(n, k, a) else 'NO')
