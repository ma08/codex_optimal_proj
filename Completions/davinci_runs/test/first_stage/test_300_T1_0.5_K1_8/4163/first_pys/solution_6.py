

n = int(input())

dice = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-2):
    if dice[i] == dice[i+1] and dice[i+1] == dice[i+2]:
        print("Yes")
        exit()

print("No")