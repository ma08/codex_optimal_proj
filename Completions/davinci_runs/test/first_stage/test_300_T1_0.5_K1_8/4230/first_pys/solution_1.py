

from sys import stdin

def main():
    x, n = map(int, stdin.readline().split())
    p = set(map(int, stdin.readline().split()))

    ans = float('inf')
    for i in range(x-n, x+n+1):
        if i not in p:
            ans = min(ans, i)
    print(ans)

if __name__ == '__main__':
    main()