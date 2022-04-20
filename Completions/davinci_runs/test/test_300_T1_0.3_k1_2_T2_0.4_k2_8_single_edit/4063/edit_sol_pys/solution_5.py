
import sys

def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    d.reverse()
    ans = 0
    for i in range(N // 2):
        if d[i] == d[i + N // 2]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
