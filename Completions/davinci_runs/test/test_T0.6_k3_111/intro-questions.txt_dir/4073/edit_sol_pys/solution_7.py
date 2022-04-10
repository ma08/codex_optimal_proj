

from functools import wraps

def memoize(f):
    memo = {}
    @wraps(f)
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(raw_input())
array = map(int, raw_input().split())

fib_array = [fibonacci(i) for i in range(max(array))]

total = 0
for i in array:
    total += fib_array[i-1]
print total % 1000000007
