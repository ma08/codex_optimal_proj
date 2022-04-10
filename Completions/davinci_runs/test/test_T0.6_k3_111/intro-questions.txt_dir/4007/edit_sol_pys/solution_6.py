

n = int(input())
friends_list = [int(x) for x in input().split()]
for i in range(n-1):
    if friends_list[i] == 0 and friends_list[i-1] != 0:
        friends_list[i] = friends_list[i-1] + 1
    elif friends_list[i] == 0:
        friends_list[i] = 1
print(friends_list)
