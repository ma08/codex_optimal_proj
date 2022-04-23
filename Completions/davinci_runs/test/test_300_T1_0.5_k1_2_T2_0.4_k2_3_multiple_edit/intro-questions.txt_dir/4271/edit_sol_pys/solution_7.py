
n = int(input()) # number of elements
dishes = list(map(int, input().split())) # elements
points = list(map(int, input().split())) # points for each element
bonus = list(map(int, input().split())) # bonus for each element

ans = 0
for i in range(n):
    ans += points[dishes[i] - 1] # add points for each element
    if i > 0 and dishes[i] == dishes[i - 1] + 1: # if element is next to previous element
        ans += bonus[dishes[i - 1] - 1] # add bonus for previous element

print(ans)
