

import fileinput

n = int(input())
friends_list = [int(x) for x in input().split()]

print(friends_list.index(min(friends_list)) + 1)
