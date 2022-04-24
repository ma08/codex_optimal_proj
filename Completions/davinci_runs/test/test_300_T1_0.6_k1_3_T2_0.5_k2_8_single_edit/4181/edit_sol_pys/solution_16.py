
# Solved by Tashfia Rahman

n = int(input())

attack = list(map(int, input().split())) #attack = [3,4,5,6]
defend = list(map(int, input().split())) #defend = [2,3,4,5]

attack.sort(reverse=True)
defend.sort(reverse=True)

sum = 0

for i in range(n):
    if attack[i] > defend[i]:
        sum = sum + defend[i]
    else:
        sum = sum + attack[i]

print(sum)
