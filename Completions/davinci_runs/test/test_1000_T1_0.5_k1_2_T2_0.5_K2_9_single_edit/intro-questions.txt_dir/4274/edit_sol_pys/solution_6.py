

n, m, k = map(int, input().split())

if n == m == k:
    print("Yes")
elif n == m or n == k or m == k:
    print("Yes")
else:
    print("No")
