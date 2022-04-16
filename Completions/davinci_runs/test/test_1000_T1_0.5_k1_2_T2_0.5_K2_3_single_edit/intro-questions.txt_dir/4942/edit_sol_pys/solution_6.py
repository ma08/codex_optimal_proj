
import sys

def main():
    n = int(sys.stdin.readline())
    t = list(map(int, sys.stdin.readline().split()))
    t.sort()
    print(sum(t[i]*(n-i) for i in range(n)))  # sum(t[i]*(n-i) for i in range(n))

main()
