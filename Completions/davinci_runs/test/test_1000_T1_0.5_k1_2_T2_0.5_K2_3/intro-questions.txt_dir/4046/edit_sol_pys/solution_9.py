

import sys

def get_input():
    n = int(input())
    p = [int(x) for x in input().split()]
    return n, p

def check_permutation(n, p):
    if n == 1:
        return True
    if len(p) != n:
        return False
    for i in p:
        if abs(i) >= n:
            return False
    return True

def create_permutation(n, p):
    if n == 1:
        return [1]
    q = [0] * n
    q[0] = p[0]
    q[1] = p[0] + p[1]
    for i in range(2, n):
        q[i] = q[i-1] + p[i-1]
    return q

def print_permutation(p):
    print(" ".join([str(x) for x in p]))

def main():
    n, p = get_input()
    if not check_permutation(n, p):
        print(-1)
        return
    q = create_permutation(n, p[1:])
    print_permutation(q)

if __name__ == "__main__":
    main()
