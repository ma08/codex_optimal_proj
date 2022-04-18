import sys
N = int(sys.stdin.readline())
d_list = [int(sys.stdin.readline()) for i in range(N)]
print(len(set(d_list)))
