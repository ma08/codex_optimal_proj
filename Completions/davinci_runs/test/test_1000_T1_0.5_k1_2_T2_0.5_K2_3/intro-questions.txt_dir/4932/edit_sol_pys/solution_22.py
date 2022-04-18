import sys

def main():
    N, M, K = map(int, sys.stdin.readline().split())
    if N + M >= K and N <= K and M <= K and N + M - K >= 0:
        print('Yes')
    else:
        print('No')

main()
