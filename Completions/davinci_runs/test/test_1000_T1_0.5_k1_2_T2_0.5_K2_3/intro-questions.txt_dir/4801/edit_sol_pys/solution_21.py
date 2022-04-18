

# Solution

# we are looking for the longest increasing sub-sequence
# the idea is to store the longest increasing sub-sequence that ends at a certain index
# the longest sub-sequence that ends at i is the longest sub-sequence that ends at i-1 and a_i
# we are looking for the longest sub-sequence that ends at the last index
# we store the length of the longest sub-sequence that ends at index i in dp[i]
# we also store the index of the last element of the longest sub-sequence that ends at index i in last[i]
# dp[0] = 1, last[0] = 0
# dp[i] = dp[i-1] + 1 if a[i] > a[last[i-1]] else dp[i-1]            # update the length of the longest sub-sequence that ends at i
# last[i] = i if dp[i] > dp[i-1] else last[i-1]  # update the index of the last element of the longest sub-sequence that ends at i
# the longest sub-sequence ends at the index of the longest sub-sequence that ends at the last index
# we use the last array to backtrack and find the elements of the longest sub-sequence
# we start at last[last[n-1]] and add the element at that index to the sub-sequence
# then we move to the index that is stored at last[last[n-1]]
# and so on until we reach 0

# read input
n = int(input())
a = list(map(int, input().split()))

# initialise the arrays
dp = [1 for _ in range(n)]
last = [i for i in range(n)]

# loop over the array
for i in range(1, n):
    # if the current element is greater than the last element of the longest sub-sequence that ends at i-1
    # then the longest sub-sequence that ends at i is the longest sub-sequence that ends at i-1 plus the current element
    # otherwise it is the same as the longest sub-sequence that ends at i-1
    if a[i] > a[last[i-1]]:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]
    # if the length of the longest sub-sequence that ends at i is greater than the length of the longest sub-sequence that ends at i-1
    # then the last element of the longest sub-sequence that ends at i is the current element
    # otherwise it is the same as the last element of the longest sub-sequence that ends at i-1
    if dp[i] > dp[i-1]:
        last[i] = i
    else:
        last[i] = last[i-1]

# print the length of the longest subsequence
print(dp[n-1])

# backtrack to find the elements of the longest subsequence
# start at the index of the last element of the longest subsequence that ends at the last index
i = last[n-1]
# initialise the subsequence
subseq = []
# loop over the array
while i >= 0:
    # add the element at the current index to the subsequence
    subseq.append(a[i])
    # move to the index of the last element of the longest subsequence that ends at the current index
    i = last[i]
# reverse the subsequence
subseq.reverse()
# print the subsequence
print(" ".join(map(str, subseq)))
