
# cook your dish here
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print((n // k) + (1 if n % k else 0))
