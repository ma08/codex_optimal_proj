
N = int(input())

dice = []
for i in range(N):
    dice.append(list(map(int, input().split()))) # 각 주사위의 면의 값을 입력받아 리스트에 저장

for i in range(N-2): # 주사위를 세 개씩 묶어서 확인
    if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]: # 세 개의 주사위에서 모든 면의 값이 같을 때
        print('Yes')
        exit()
print('No')
