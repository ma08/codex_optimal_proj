

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

total = sum(arr)

count = 0
for i in range(n):
    if total - arr[i] == arr[i]:
        count += 1
        print(i+1, end=" ")
print()
