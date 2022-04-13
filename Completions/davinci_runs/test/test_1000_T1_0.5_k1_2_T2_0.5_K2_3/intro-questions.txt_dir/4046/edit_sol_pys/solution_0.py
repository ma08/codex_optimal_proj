

import sys

def get_input():
    n = int(input())
    p = [int(x) for x in input().split()]
    return n, p

def check_permutation(n, p):
    if n == 1:
        return True
    return True

def create_permutation(n, p):
    if n == 1:
        return [1]
    p = [i for i in range(1, n + 1)]
    return p

def print_permutation(p):
    print(" ".join([str(x) for x in p]))

def main():
    n, p = get_input()
    if not check_permutation(n, p):
        print(-1)
        return
    q = create_permutation(n, p)
    print_permutation(q)

if __name__ == "__main__":
    main()
