

import fileinput, sys

n = int(sys.stdin.readline())
friends_list = [int(x) for x in sys.stdin.readline().split()]

print(friends_list.index(max(friends_list)) + 1)
