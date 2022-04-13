
import sys

def readline():
    return sys.stdin.readline().strip()

def main():
    N = int(readline())
    A = [int(x) for x in readline().split()]

    s_a = sum(A)
    if s_a % N == 0:
        print(s_a // N)
    else:
        print(s_a // N + 1)

if __name__ == '__main__':
    main()
