


# Problem: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/little-monk-and-good-string/
# Solved by Tashfia Rahman

n = int(input())

arr = list(map(int, input().split()))

arr.sort(reverse=True)

sum = 0

for i in range(n):
    if arr[i] > arr[i+1]:
        sum = sum + arr[i+1]
    else:
        sum = sum + arr[i]

print(sum)
