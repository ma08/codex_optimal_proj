# -*- coding: utf-8 -*-

# Get input
N, M = map(int, input().split())

# Init
food_list = [[] for _ in range(N)]
for i in range(N):
    K = int(input().split()[0])
    food_list[i] = list(map(int, input().split()))

# Main
answer = 0
for i in range(1, M+1):
    if all(i in food for food in food_list): # i가 모든 food_list에 있으면
        answer += 1
print(answer)
