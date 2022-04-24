

n = int(input())
a = list(map(int, input().split()))

arr = [0] * n

for i in range(n):
    arr[a[i]-1] = i+1

for i in arr:
    print(i)
