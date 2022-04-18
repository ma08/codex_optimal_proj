

n, k = map(int, input().split())
a = list(map(int, input().split()))

# build array of people in order, we need to know how many people are in front of us
# to know how many people we have to wait for
people = [0] * (n + 1)
for i in range(n):
    people[a[i]] = i + 1

# print the number of people we have to wait for
print(sum(people[i] for i in range(k + 1)))
