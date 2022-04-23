# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.


# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

# SOLUTION 1:

# Get the input
n,k = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

# Make a hashmap to store the frequency of the elements
freq = collections.defaultdict(int)

# Store the frequency of the elements
for i in s:
    freq[i] += 1

# Get the most frequent element in the array
max_freq = max(freq.values())

# Get the element with the maximum frequency
max_freq_elem = [k for k,v in freq.items() if v==max_freq]

# Get the first element that has the maximum frequency
max_freq_elem = max_freq_elem[0]

# Get the first k elements of the array
t = s[:k]

# Initialize the result
result = []

# Initialize the maximum frequency
max_freq = 0

# Initialize the maximum frequency element
max_freq_elem = 0

# Initialize the window
window_start = 0

# Get the frequency of the first k elements
for i in t:
    freq[i] -= 1

# Get the maximum frequency in the sub-array
max_freq = max(freq.values())

# Get the element with the maximum frequency in the sub-array
max_freq_elem = [k for k,v in freq.items() if v==max_freq]

# Get the first element that has the maximum frequency in the sub-array
max_freq_elem = max_freq_elem[0]

# Store the maximum frequency element in the result
result.append(max_freq_elem)

# Iterate through the array
for window_end in range(k,n):
    # Remove the element from the window
    freq[s[window_start]] += 1
    # Increment the window start
    window_start += 1
    # Subtract the frequency of the element in the window
    freq[s[window_end]] -= 1
    # Get the maximum frequency in the sub-array
    max_freq = max(freq.values())
    # Get the element with the maximum frequency in the sub-array
    max_freq_elem = [k for k,v in freq.items() if v==max_freq]
    # Get the first element that has the maximum frequency in the sub-array
    max_freq_elem = max_freq_elem[0]
    # Store the maximum frequency element in the result
    result.append(max_freq_elem)

# Print the result
print(*result)
