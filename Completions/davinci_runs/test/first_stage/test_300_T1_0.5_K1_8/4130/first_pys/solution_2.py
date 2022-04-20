

# SOLUTION
# This problem can be solved using a greedy algorithm.
# We sort the array of weights and then we iterate through the array.
# If the next weight is different from the previous one, we add it to the team.
# If the next weight is the same as the previous one, we check if we can change it,
# and if it is possible, we add it to the team.

# We use a set to check if the weight already exists.

# We use a variable to store the previous weight.

# We use a variable to store the number of boxers in the team.

# We sort the array of weights.

# We iterate through the array of weights.

# If the current weight is different from the previous weight, we add it to the team.

# If the current weight is the same as the previous weight, we check if we can change it.

# If we can change the current weight, we add it to the team.


n = int(input())
a = list(map(int, input().split()))

a.sort()

s = set()

prev = -1
ans = 0

for i in a:
    if i != prev:
        ans += 1
        s.add(i)
    elif i - 1 not in s:
        ans += 1
        s.add(i - 1)
    prev = i

print(ans)