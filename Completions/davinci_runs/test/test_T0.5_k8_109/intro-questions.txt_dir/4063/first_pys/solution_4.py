

#Input
N = int(input())
difficulties = list(map(int, input().split()))

#Initialize
difficulties.sort()

#Process
ARCs = 0
ABCs = 0

for difficulty in difficulties:
    if difficulty >= difficulties[N//2]:
        ARCs += 1
    else:
        ABCs += 1

print(ARCs)