

# Solution

# the idea is to store the longest increasing subsequence that ends at a certain index
# the longest subsequence that ends at i is the longest subsequence that ends at i-1 and a_i or a_i
# we are looking for the longest subsequence that ends at the last index and we store it in dp[n-1]
# we store the length of the longest subsequence that ends at index i in dp[i]
# dp[i] = max(dp[j] + 1 if a[i] > a[j] else 1 for j in range(i))
# we also store the index of the last element of the longest subsequence that ends at index i in last[i]
# last[i] = argmax(dp[j] + 1 if a[i] > a[j] else 1 for j in range(i))
# we then use the last array to backtrack and find the elements of the longest subsequence
# we start at last[n-1] and add the element at that index to the subsequence
# then we move to the index that is stored at last[last[n-1]]
# and so on until we reach 0, the index of the last element of the longest subsequence that ends at the first index

# read input
n = int(input())
a = list(map(int, input().split()))

# initialise the arrays, dp[0] = 1, last[0] = 0
dp = [1]
last = [0]

# loop over the array, starting at the second element
for i in range(1, n):
    # initialise the length of the longest increasing subsequence that ends at the current index
    # to the length of the longest increasing subsequence that ends at the previous index
    # or 1 if the current element is less than the last element of the longest subsequence that ends at the previous index
    dp.append(max(dp[j] + 1 if a[i] > a[j] else 1 for j in range(i)))
    # initialise the index of the last element of the longest subsequence that ends at the current index
    # to the index of the last element of the longest subsequence that ends at the previous index
    # or the current index if the current element is greater than the last element of the longest subsequence that ends at the previous index
    last.append(i if dp[i] > dp[i-1] else last[i-1])

# print the length of the longest subsequence
print(dp[n-1])

# backtrack to find the elements of the longest subsequence
# start at the index of the last element of the longest subsequence that ends at the last index
i = last[n-1]
# initialise the subsequence
subseq = []
# loop over the array, starting at the last index
while i >= 0:
    # add the element at the current index to the subsequence
    subseq.append(a[i])
    # move to the index of the last element of the longest subsequence that ends at the current index
    i = last[i]
# reverse the subsequence
subseq.reverse()
# print the subsequence
print(" ".join(map(str, subseq)))
