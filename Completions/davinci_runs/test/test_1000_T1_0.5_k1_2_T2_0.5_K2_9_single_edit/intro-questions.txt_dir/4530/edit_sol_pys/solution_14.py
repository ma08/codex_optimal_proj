

# SOLUTION
# This problem can be solved using a simple greedy approach. We will iterate over the skills and we will try to add them to the first 
# team. If the skill is already in the first team, we will add it to the second team. If the skill is already in the second team, we 
# will skip it. The answer is the size of the first team.
#
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))
  first_team = set()
  second_team = set()
  for i in range(n):
    if a[i] not in first_team:
      first_team.add(a[i])
    elif a[i] not in second_team:
      second_team.add(a[i])
  print(len(first_team))
