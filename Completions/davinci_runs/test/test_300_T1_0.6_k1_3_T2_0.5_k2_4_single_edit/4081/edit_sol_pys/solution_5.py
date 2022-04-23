

n = int(input())
a = [int(x) for x in input().split()]

# In the optimal solution the sequence must be strictly increasing.
# We can find the longest strictly increasing subsequence in O(n log n) time.
# (See https://en.wikipedia.org/wiki/Longest_increasing_subsequence#Efficient_algorithms)
#
# The optimal solution then consists of the longest strictly increasing subsequence
# followed by the remaining elements from the original sequence.

# Find the longest increasing subsequence.
# We use a list to store the indices of the sequence.
# The indices are sorted according to the corresponding elements in the sequence.
# The last element of the list is the smallest element of the longest increasing subsequence.
# If a new element is larger than the last element in the list, we append it to the list.
# Otherwise, we replace the smallest element that is larger than the new element
# with the new element.
# This way the list always represents the longest increasing subsequence.
lis = []
for i in range(n):
    if lis == [] or a[i] > a[lis[-1]]:
        lis.append(i)
    elif a[i] > a[lis[-1]]:
        lis.append(i)
    else:
        for j in range(len(lis)):
            if a[lis[j]] > a[i]:
                lis[j] = i
                break

# Construct the solution from the longest increasing subsequence.
s = ['L' for _ in range(len(lis))]
left = [0] * n
for i in range(len(lis)):
    left[lis[i]] = 1
    if i > 0:
        left[lis[i]] += left[lis[i-1]]

for i in range(len(lis)):
    if i == len(lis) - 1 or left[lis[i]] < left[lis[i+1]]:
        s[i] = 'R'

# Print the answer.
print(len(lis))
print(''.join(s))
