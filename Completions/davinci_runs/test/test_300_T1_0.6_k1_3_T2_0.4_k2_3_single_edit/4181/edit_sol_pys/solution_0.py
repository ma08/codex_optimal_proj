

# Solved by Tashfia Rahman

n = int(input())

attack = list(map(int, input().split()))
defence = list(map(int, input().split()))

attack.sort(reverse=True)
defence.sort(reverse=True)

sum = 0

for i in range(n):
    if attack[i] > defence[i]:
        sum = sum + defence[i]
    else:
        sum = sum + attack[i]

print(sum)
