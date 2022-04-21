

# my solution to https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
import sys

# read the input
a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

# create a dictionary of characters that appear in a
a_dict = {}
for c in a:
    if c in a_dict:
        a_dict[c] += 1
    else: a_dict[c] = 1

# count the number of characters that appear only in b
count = len(b)
for c in b:
    if c in a_dict:
        count -= 1

# print the result (the minimum number of deletions)
print(count)
