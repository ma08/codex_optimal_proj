import sys

def main():
    e, f, c = map(int, sys.stdin.readline().split()) # read input
    print(solve(e, f, c)) # print result

def solve(e, f, c):
    """
    Return the number of sodas drunk on an extra thirsty day.
    """
    total = e + f
    drunk = 0
    while total >= c:
        drunk += total // c
        total = total % c + total // c
    return drunk

if __name__ == '__main__':
    main()
