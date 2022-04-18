

# #Program for finding best horror movie
# n,h,l = map(int,input().split())
# horror_list = list(map(int,input().split()))
# similar = {}
# for _ in range(l):
#     a,b = map(int,input().split())
#     if a not in similar:
#         similar[a] = [b]
#     else:
#         similar[a].append(b)
#     if b not in similar:
#         similar[b] = [a]
#     else:
#         similar[b].append(a)

# hi = [0]*n
# for i in horror_list:
#     hi[i] = 0
# for i in horror_list:
#     for j in similar[i]:
#         if hi[j] == 0:
#             continue
#         elif hi[j] == 1:
#             hi[j] = 0
#         else:
#             hi[j] = 1

# max_hi = max(hi)
# max_hi_movies = []
# for i in range(n):
#     if hi[i] == max_hi:
#         max_hi_movies.append(i)
# print(min(max_hi_movies))

def max_subarray_sum(a,size):
    max_so_far = 0
    max_ending_here = 0
    for i in range(0,size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
    return max_so_far

def max_subarray_sum_all_positive(a,size):
    max_so_far = 0
    for i in range(0,size):
        max_so_far = max_so_far + a[i]
    return max_so_far

def max_subarray(a,size):
    max_sum = max_subarray_sum(a,size)
    if max_sum == 0:
        max_sum = max_subarray_sum_all_positive(a,size)
    return max_sum

# Driver program to test maxSubArraySum
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum contiguous sum is", max_subarray(a,len(a)))
