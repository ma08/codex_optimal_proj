import sys
sys.setrecursionlimit(10 ** 7)
def main():
    N = int(input())
    A = list(map(int, input().split()))[::-1]
    def f(i, total):
        if i == N:
            return total
        else:
            return f(i + 1, total + A[i])
    print(f(0, 0))

if __name__ == '__main__':
    main()
