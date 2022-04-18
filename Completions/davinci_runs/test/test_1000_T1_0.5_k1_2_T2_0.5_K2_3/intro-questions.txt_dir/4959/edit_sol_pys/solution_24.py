
import sys

def main():
    e, f, c = map(int, sys.stdin.readline().split())
    print(solve(e, f, c))

def solve(e, f, c):
    """
    Return the number of sodas drank on an extra-thirsty day.
    """
    total = e + f
    drank = 0
    while total >= c:
        drank += total // c
        total = total % c + total // c
    return drank

if __name__ == '__main__':
    main()
