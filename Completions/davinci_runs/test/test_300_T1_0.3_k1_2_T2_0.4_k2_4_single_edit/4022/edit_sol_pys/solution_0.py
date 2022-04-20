
# Solution

n = int(input())  # input the number of the lines

left = []  # list of left points
right = []  # list of right points

for i in range(n):
    l, r = map(int, input().split())  # input the coordinates of the lines
    left.append(l)
    right.append(r)

left.sort()  # sort the list of left points
right.sort()  # sort the list of right points

if n == 2:  # if there are only 2 lines
    print(right[1] - left[0])
else:  # if there are more than 2 lines
    print(max(right[n - 2] - left[0], right[n - 1] - left[1], right[n - 1] - left[0]))
