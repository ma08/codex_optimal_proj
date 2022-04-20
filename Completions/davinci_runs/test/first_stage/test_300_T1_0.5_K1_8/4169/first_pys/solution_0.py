

import sys

def solve(n, m, a, b):
    m_left = m
    cost = 0
    for i in range(n):
        if m_left > b[i]:
            cost += a[i] * b[i]
            m_left -= b[i]
        else:
            cost += a[i] * m_left
            m_left = 0
            break
    return cost

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    print(solve(n, m, a, b))

if __name__ == '__main__':
    main()