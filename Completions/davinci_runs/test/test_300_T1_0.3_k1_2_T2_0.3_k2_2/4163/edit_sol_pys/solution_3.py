
N = int(input())

dice = []
for i in range(N):
    dice.append(list(map(int, input().split()))) # dice = [[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]

for i in range(N-2):
    if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
        print('Yes')
        exit()
print('No')
