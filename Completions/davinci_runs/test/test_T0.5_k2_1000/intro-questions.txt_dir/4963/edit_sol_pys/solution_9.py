
n = int(input())
d = list(map(int, input().split()))

# build array of people in order (people[i] = j means that i-th person is standing in front of j-th person)
people = [0] * n
for i in range(1, n):
    people[d[i-1]] = i

# print people in order
print(*people)
