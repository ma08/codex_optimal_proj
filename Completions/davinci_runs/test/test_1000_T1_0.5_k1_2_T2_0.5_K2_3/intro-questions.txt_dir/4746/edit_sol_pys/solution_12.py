"""
This is my solution to the problem described at
https://www.hackerrank.com/contests/projecteuler/challenges/euler039/problem
"""

import sys

def possible(p_max, perimeters):
    """
    >>> possible(1000, [120, 60, 30, 24, 20, 18, 16, 15, 12, 10, 9, 8, 6, 5, 4, 3, 2])
    840
    """
    solutions = {}
    for p in perimeters:
        for a in range(1, p + 1):
            for b in range(1, p + 1):
                if a + b >= p:
                    break
                c = p - a - b
                if a*a + b*b == c*c:
                    if p not in solutions:
                        solutions[p] = 0
                    solutions[p] += 1
    max_solutions = 0
    for p in solutions:
        if solutions[p] > max_solutions:
            max_solutions = solutions[p]
            best_p = p
    return best_p

if __name__ == "__main__":
    p_max = int(sys.stdin.readline().strip())
    perimeters = list(map(int, sys.stdin.readline().split()))
    print(possible(p_max, perimeters))
