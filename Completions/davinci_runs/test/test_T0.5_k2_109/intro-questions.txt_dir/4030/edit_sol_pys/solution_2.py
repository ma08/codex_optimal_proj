
import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

# read data for n sequences
n = int(input())

seq = input()

# if there are only one type of char, then the answer is 1
if len(set(seq)) == 1:
    print(1)
    print(" ".join(["1"] * n))
    exit()

# create a dictionary of lists of indices for each char
# O(n)
char_dict = defaultdict(list)
for i, c in enumerate(seq):
    char_dict[c].append(i)

# create a list of chars sorted by the number of indices in descending order
# O(n)
char_list = sorted(char_dict.keys(), key=lambda c: len(char_dict[c]), reverse=True)

# create a dictionary of chars and their colors
# O(n)
char_color = {char_list[0]: 1}
for i in range(1, len(char_list)):
    prev_char = char_list[i-1]
    prev_color = char_color[prev_char]
    # if the previous char has more indices than the current one,
    # then the current char can be colored with the same color
    if len(char_dict[prev_char]) > len(char_dict[char_list[i]]):
        char_color[char_list[i]] = prev_color
    # otherwise, the current char has to be colored with a different color
    else:
        char_color[char_list[i]] = prev_color + 1

# create a list of integers that represent the colors of the chars
# O(n)
color_list = [char_color[c] for c in seq]

# print the minimum number of colors and the coloring
print(max(color_list))
print(" ".join(map(str, color_list)))
