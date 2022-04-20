
import sys

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    print(abs(p.index(n) - q.index(n)))

if __name__ == '__main__':
    main()
