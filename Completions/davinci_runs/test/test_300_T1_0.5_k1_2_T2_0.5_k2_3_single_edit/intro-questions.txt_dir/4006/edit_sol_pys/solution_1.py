import sys
sys.setrecursionlimit(10**9)

def f(n, memo):
    if n in memo:
        return memo[n]
    else:
        memo[n] = f(n+1, memo)
        while memo[n] % 10 == 0:
            memo[n] = memo[n] // 10
        return memo[n]

def main():
    n = int(input())
    memo = {0:0}
    c = 1
    while True:
        n = f(n, memo)
        if n == 0:
            print(c)
            return
        else:
            c += 1

if __name__ == "__main__":
    main()
