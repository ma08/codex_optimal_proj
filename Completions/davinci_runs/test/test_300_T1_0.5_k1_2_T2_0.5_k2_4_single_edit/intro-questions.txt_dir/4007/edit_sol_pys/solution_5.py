
n = int(input())
arr = list(map(int, input().split()))

i = 1
while i <= n:
    if arr[i - 1] == 0:
        arr[i - 1] = i
    i += 1

i = 1
while i <= n:
    if arr[i - 1] != i:
        print("NO")
        break
    i += 1

print("YES")
