

import sys

def mod_sum(a, n):
    return sum([n % i for i in a])

def solve(a):
    n = len(a)
    max_mod_sum = -1
    for i in range(n):
        max_mod_sum = max(max_mod_sum, mod_sum(a, a[i]))
    return max_mod_sum

def main():
    n = int(sys.stdin.readline())
    a = [int(i) for i in sys.stdin.readline().split()]
    print(solve(a))

if __name__ == '__main__':
    main()