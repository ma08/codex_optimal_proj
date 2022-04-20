

import sys

def main():
    n, g = map(int, input().split())
    problems = []
    for _ in range(n):
        p, c = map(int, input().split())
        problems.append((p, c))
    # print(problems)

    # solve
    problems.reverse()
    solved = 0
    for p, c in problems:
        if g <= 0:
            break
        if c > g:
            continue
        solved += g // c
        g -= (g // c) * c
    print(solved)

if __name__ == '__main__':
    main()