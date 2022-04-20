

n = int(input())
friends = list(map(int, input().split()))

# Print out the friends who have a gift
for i in range(n):
    if friends[i] != 0:
        print(i + 1, end=" ")
