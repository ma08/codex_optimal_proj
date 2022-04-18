

n = int(input())
d = list(map(int, input().split()))

# build array of people in order, starting at 1
people = [0] * (n+1)
for i in range(1, n+1):
    people[d[i-1]] = i+1

# print people
print(*people)
