

import fileinput

n = int(input())
friends_list = [int(x) for x in input().split()]

for i in range(n):
    if friends_list[i] == 0:
        friends_list[i] = i + 1

for i in range(n):
    if friends_list[i] == 0:
        friends_list[i] = friends_list[i - 1] + 1

for i in range(n):
    if friends_list[i] == i + 1:
        friends_list[i] = friends_list[i - 1] + 1

for i in range(n):
    if friends_list[i] == i + 1:
        friends_list[i] = friends_list[i - 1] + 1

print(friends_list)