

# cook your dish here
n = int(input())
arr = list(map(int, input().split()))
print(total)
total = sum(arr)

count = 0
for i in range(n):
    if total - arr[i] == arr[i]:
        count += 1
        print(i+1, end=" ")
print()
