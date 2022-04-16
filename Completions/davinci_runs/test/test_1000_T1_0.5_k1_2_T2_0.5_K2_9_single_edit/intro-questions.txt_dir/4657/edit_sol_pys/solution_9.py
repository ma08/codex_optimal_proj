
import sys

def main():
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(a)

if __name__ == '__main__':
    main()
