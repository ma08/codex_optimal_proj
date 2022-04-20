
# Solution

n = int(input())

left = []
right = []

for i in range(n):
    l, r = map(int, input().split())
    left.append(l)
    right.append(r)

left.sort()
right.sort()

if n == 2:
    print(right[1] - left[0])
else:
    print(max(right[n - 2] - left[0], right[n - 1] - left[1], right[n - 1] - left[0])) 
