import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    P = [int(i) for i in input().split()]
    ans = 0
    for i in range(0, N):
        if P[i] == i + 1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
