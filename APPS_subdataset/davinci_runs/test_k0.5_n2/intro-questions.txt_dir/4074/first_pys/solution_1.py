

# cook your dish here
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n == k:
        print(1)
    elif n < k:
        print(n)
    else:
        if n % 2 == 0:
            print(2)
        else:
            print(3)