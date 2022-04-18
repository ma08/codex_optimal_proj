
import sys

def main():
    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()

    if can_eq(s, t):
        print('Yes')
    else:
        print('No')

def can_eq(s,t):
    return sorted(s) == sorted(t)

if __name__ == '__main__':
    main()
