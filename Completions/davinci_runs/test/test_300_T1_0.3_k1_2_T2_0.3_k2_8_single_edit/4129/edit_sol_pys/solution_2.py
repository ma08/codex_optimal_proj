
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    a.sort()
    b.sort(reverse=True)
    print('YES' if sum(a[i]*b[i] for i in range(m)) >= 0 else 'NO')

main()
