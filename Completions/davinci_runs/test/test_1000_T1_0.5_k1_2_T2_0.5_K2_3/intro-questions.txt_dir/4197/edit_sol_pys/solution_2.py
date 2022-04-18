import sys
sys.setrecursionlimit(10**6)

def main():
    N, K = map(int, input().split())
    A = [int(i) for i in input().split()] + [0]

    def f(n):
        if n == 0:
            return 0
        else:
            return f(n-1) + A[n]

    print(max(f(i+K) - f(i) for i in range(N)))


if __name__ == '__main__':
    main()
