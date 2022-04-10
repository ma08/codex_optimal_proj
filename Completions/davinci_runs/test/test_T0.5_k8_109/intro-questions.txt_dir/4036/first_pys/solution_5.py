

# SOLUTION
n, k = map(int, input().split())

if n >= k:
    print("YES")
    for i in range(k):
        print(1, end=' ')
    print()
else:
    print("NO")