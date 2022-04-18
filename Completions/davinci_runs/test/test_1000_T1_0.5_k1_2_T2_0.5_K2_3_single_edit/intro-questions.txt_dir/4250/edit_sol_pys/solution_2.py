

# SOLUTION

# The solution is getting the most frequent element in the array and then going through the array to find the most frequent element in the subarray
# We will use a hash map to store the frequency of the elements and then use a sliding window technique to find the maximum frequency element in the subarray

import sys
import collections

# Get the input
n,k = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

# Make a hash map to store the frequency of the elements
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

# Get the maximum frequency
max_freq = max(freq.values())

# Get the element with the maximum frequency
max_freq_elem = [k for k,v in freq.items() if v==max_freq]

# Get the first element that has the maximum frequency
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
    # Get the maximum frequency
    max_freq = max(freq.values())
    # Get the element with the maximum frequency
    max_freq_elem = [k for k,v in freq.items() if v==max_freq]
    # Get the first element that has the maximum frequency
    max_freq_elem = max_freq_elem[0]
    # Store the maximum frequency element in the result
    result.append(max_freq_elem)

# Print the result
print(*result)
