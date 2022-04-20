
import sys

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(sum(a[:k]))

if __name__ == '__main__':
    main()
