
n = int(input())
arr = [int(input()) for _ in range(n)]
print(*[max(arr) for x in arr])
