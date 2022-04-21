

import sys
from heapq import *
# num = int(input())
# v = list(map(int, input().split()))
# heapify(v)
#
# for i in range(num-1):
#     x = heappop(v)
#     y = heappop(v)
#     heappush(v, (x+y)/2)
#
# print(v[0])

# import sys
# import heapq
#
# num = int(sys.stdin.readline())
# v = list(map(int, sys.stdin.readline().split()))
# heapq.heapify(v)
#
# for i in range(num-1):
#     x = heapq.heappop(v)
#     y = heapq.heappop(v)
#     heapq.heappush(v, (x+y)/2)
#
# print(v[0])

# def solution(n, data):
#     answer = 0
#     temp_data = list()
#     for i in range(n):
#         temp_data.append(data[i])
#
#     for i in range(n):
#         temp_data.sort()
#         temp_data[0] = (temp_data[0]+temp_data[1])/2
#         del temp_data[1]
#         answer = temp_data[0]
#     return answer
#
# if __name__ == '__main__':
#     n = int(input())
#     data = list(map(int, input().split()))
#     print(solution(n, data))

# def solution(s):
#     answer = 0
#     temp_data = list()
#     for i in range(len(s)):
#         temp_data.append(s[i])
#
#     for i in range(len(s)):
#         temp_data.sort()
#         temp_data[0] = (temp_data[0]+temp_data[1])/2
#         del temp_data[1]
#         answer = temp_data[0]
#     return answer
#
# if __name__ == '__main__':
#     n = int(input())
#     s = list(map(int, input().split()))
#     print(solution(s))

def solution(n, data):
    answer = 0
    temp_data = list()
    for i in range(n):
        temp_data.append(data[i])

    for i in range(n):
        temp_data.sort()
        temp_data[0] = (temp_data[0]+temp_data[1])/2
        del temp_data[1]
        answer = temp_data[0]
    return answer

if __name__ == '__main__':

num = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
print(solution(num, data))
