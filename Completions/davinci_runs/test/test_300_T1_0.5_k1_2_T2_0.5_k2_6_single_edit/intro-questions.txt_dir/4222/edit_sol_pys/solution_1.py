

import sys

    import sys
def main():
    print(n, k)
    n, k = map(int, sys.stdin.readline().split())
    print(victim)
    victim = set([i for i in range(1, n+1)])
    for _ in range(k):
        print(d)
        d = int(sys.stdin.readline())
        print(victim)
        victim -= set(map(int, sys.stdin.readline().split()))
    print(len(victim))

if __name__ == '__main__':
    main()
