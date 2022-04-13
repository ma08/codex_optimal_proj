

# import sys

# [N, S, R] = map(int, sys.stdin.readline().split())
# damaged = map(int, sys.stdin.readline().split())
# reserve = map(int, sys.stdin.readline().split())

# def check(reserve, damaged):
#     for i in damaged:
#         if i-1 in reserve or i+1 in reserve:
#             reserve.remove(i-1)
#             reserve.remove(i+1)
#             damaged.remove(i)
#     return len(damaged)

# print check(reserve, damaged)

# a = [1,2,3]
# b = [1,2,3]
# if a == b:
#     print "yes"
# else:
#     print "no"

# import sys

# [N, M] = map(int, sys.stdin.readline().split())
# nums = map(int, sys.stdin.readline().split())
# nums.sort()

# def binarySearch(start, end, num):
#     if start > end:
#         return -1
#     mid = (start+end)/2
#     if nums[mid] == num:
#         return mid
#     elif nums[mid] > num:
#         return binarySearch(start, mid-1, num)
#     else:
#         return binarySearch(mid+1, end, num)

# for i in range(M):
#     num = int(sys.stdin.readline())
#     print binarySearch(0, N-1, num)+1

# import sys

# [N, M] = map(int, sys.stdin.readline().split())
# nums = map(int, sys.stdin.readline().split())
# nums.sort()

# def binarySearch(start, end, num):
#     if start > end:
#         return -1
#     mid = (start+end)/2
#     if nums[mid] == num:
#         return mid
#     elif nums[mid] > num:
#         return binarySearch(start, mid-1, num)
#     else:
#         return binarySearch(mid+1, end, num)

# for i in range(M):
#     num = int(sys.stdin.readline())
#     print binarySearch(0, N-1, num)+1

# import sys

# [N, M] = map(int, sys.stdin.readline().split())
# nums = map(int, sys.stdin.readline().split())
# nums.sort()

# def binarySearch(start, end, num):
#     if start > end:
#         return -1
#     mid = (start+end)/2
#     if nums[mid] == num:
#         return mid
#     elif nums[mid] > num:
#         return binarySearch(start, mid-1, num)
#     else:
#         return binarySearch(mid+1, end, num)

# for i in range(M):
#     num = int(sys.stdin.readline())
#     print binarySearch(0, N-1, num)+1

# import sys

# [N, M] = map(int, sys.stdin.readline().split())
# nums = map(int, sys.stdin.readline().split())
# nums.sort()

# def binarySearch(start, end, num):
#     if start > end:
#         return -1
#     mid = (start+end)/2
#     if nums[mid] == num:
#         return mid
#     elif nums[mid] > num:
#         return binarySearch(start, mid-1, num)
#     else:
#         return binarySearch(mid+1, end, num)

# for i in range(M):
#     num = int(sys.stdin.readline())
#     print binarySearch(0, N-1, num)+1

# import sys

# [N, M] = map(int, sys.stdin.readline().split())
# nums = map(int, sys.stdin.readline().split())
# nums.sort()

# def binarySearch(start, end, num):
#     if start > end:
#         return -1
#     mid = (start+end)/2
#     if nums[mid] == num:
#         return mid
#     elif nums[mid] > num:
#         return binarySearch(start, mid-1, num)
#     else:
#         return binarySearch(mid+1, end, num)

# for i in range(M):
#     num = int(sys.stdin.readline())
#     print binarySearch(0, N-1, num)+1

# import sys

# [N, M] = map(int, sys.stdin.readline().split())
# nums = map(int, sys.stdin.readline().split())
# nums.sort()

# def binarySearch(start, end, num):
#     if start > end:
#         return -1
#     mid = (start+end)/2
#     if nums[mid] == num:
#         return mid
#     elif nums[mid] > num:
#         return binarySearch(start, mid-1, num)
#     else:
#         return binarySearch(mid+1, end, num)

# for i in range(M):
#     num = int(sys.stdin.readline())
#     print binarySearch(0, N-1, num)+1

# import sys

# [N, M] = map(int, sys.stdin.readline().split())
# nums = map(int, sys.stdin.readline().split())
# nums.sort()

# def binarySearch(start, end, num):
#     if start > end:
#         return -1
#     mid = (start+end)/2
#     if nums[mid] == num:
#         return mid
#     elif nums[mid] > num:
#         return binarySearch(start, mid-1, num)
#     else:
#         return binarySearch(mid+1, end, num)

# for i in range(M):
#     num = int(sys.stdin.readline())
#     print binarySearch(0, N-1, num)+1
