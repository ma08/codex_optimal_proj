import sys

def main():
    N, M, K = map(int, sys.stdin.readline().split())
    if N + M == K or N == K or M == K:
        print('Yes')
    else:
        print('No')

main()
