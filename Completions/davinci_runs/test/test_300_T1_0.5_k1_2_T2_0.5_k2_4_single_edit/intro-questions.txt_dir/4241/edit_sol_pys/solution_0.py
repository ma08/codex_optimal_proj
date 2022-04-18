import sys


input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] % 2 == 0:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
