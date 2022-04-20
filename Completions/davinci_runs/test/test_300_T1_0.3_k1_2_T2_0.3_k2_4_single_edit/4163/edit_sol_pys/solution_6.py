
import sys
input = sys.stdin.readline

N = int(input())

dice = []
for i in range(N):
    dice.append(list(map(int, input().rstrip().split())))

for i in range(N-2):
    if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
        print('Yes')
        exit()
print('No')
