

import sys

def get_input(n):
    p = [int(x) for x in input().split()]
    return p

def check_permutation(n, p):
    if len(p) != n:
        return False
    if n == 1:
        return True
    for i in p:
        if abs(i) >= n:
            return False
    return True

def find_cycle(p):
    pass

def main():
    n = int(input())
    p = get_input(n)
    if not check_permutation(n, p):
        print(-1)
        return

if __name__ == "__main__":
    main()
