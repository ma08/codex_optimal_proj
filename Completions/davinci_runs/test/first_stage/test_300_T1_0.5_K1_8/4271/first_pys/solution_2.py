

# Get input
n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

# Get satisfaction points
points = 0
for i in range(n):
    points += b_list[a_list[i]-1]
    if i != n-1:
        if a_list[i] == a_list[i+1]-1:
            points += c_list[a_list[i]-1]

# Print result
print(points)