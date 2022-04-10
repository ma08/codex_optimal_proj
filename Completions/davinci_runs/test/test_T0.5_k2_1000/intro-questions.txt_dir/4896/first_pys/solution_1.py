

N = int(input())
bricks = list(map(int, input().split()))

towers = 1

for i in range(1, N):
    if bricks[i] > bricks[i-1]:
        towers += 1

print(towers)