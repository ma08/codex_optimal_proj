

for i in range(int(input())):
    n, k = map(int, input().split())
    if k == 1:
        print(n)
    else:
        print(n // k + (1 if n % k else 0))