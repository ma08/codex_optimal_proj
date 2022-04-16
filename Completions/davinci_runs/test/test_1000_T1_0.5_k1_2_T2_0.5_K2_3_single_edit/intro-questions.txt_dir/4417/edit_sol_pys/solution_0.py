

# q = int(input()) # TLE
# for _ in range(q): # TLE
#     n, k = map(int, input().split()) # TLE
#     a = list(map(int, input().split())) # TLE
#     a.sort() # TLE
#     ans = -1 # TLE
#     if n == 1: # TLE
#         ans = a[0] # TLE
#     else: # TLE
#         for i in range(1, k+1): # TLE
#             if a[0] + i <= a[-1] - i: # TLE
#                 ans = a[0] + i # TLE
#                 break # TLE
#     print(ans) # TLE

q = int(input())
for _ in range(q): # TLE
    n, k = map(int, input().split()) # TLE
    a = list(map(int, input().split())) # TLE
    a.sort() # TLE
    ans = -1 # TLE
    if n == 1: # TLE
        ans = a[0] # TLE
    else: # TLE
        for i in range(1, k+1): # TLE
            if a[0] + i <= a[-1] - i: # TLE
                ans = a[0] + i # TLE
                break # TLE
    print(ans) # TLE
