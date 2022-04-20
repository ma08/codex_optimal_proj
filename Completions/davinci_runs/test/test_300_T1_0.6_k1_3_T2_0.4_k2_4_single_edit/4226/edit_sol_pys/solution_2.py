

n, m = map(int, input().split())

if n == m:
    print("Yes") if n % 2 == 0 else print("No")

if n == m + 1:
    print("Yes") if n % 2 == 1 else print("No")

if n + 1 == m:
    print("Yes") if m % 2 == 1 else print("No")
