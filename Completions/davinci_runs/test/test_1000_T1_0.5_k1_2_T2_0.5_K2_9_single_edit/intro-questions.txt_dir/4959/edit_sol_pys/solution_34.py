
import sys

def main():
    s = sys.stdin.readline()
    print(solve(s))

def solve(s):
    """
    Return the number of sodas drank on an extra thirsty day
    when the input is a string.
    """
    e, f, c = map(int, s.split())
    total = int(e) + int(f)
    drank = 0
    while total >= int(c):
        drank += total // int(c)
        total = total % int(c) + total // int(c)
    return drank

if __name__ == '__main__':
    main()
