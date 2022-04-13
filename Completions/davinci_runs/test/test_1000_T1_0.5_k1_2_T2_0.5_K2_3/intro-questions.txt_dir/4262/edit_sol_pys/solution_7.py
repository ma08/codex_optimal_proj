N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(abs(factorial(N) - P - Q))
