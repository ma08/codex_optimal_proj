
S = raw_input()

# The number of cubes that can be removed is the maximum number of zeroes that are adjacent to ones.
# Since there can be at most 10^5 cubes, we can solve this problem in O(n) time.

# The number of zeroes adjacent to ones is the number of zeroes minus the number of zeroes that are not adjacent to ones.
# The number of zeroes that are not adjacent to ones is the number of zeroes that are adjacent to other zeroes.
# The number of zeroes that are adjacent to other zeroes is the number of zeroes minus the number of zeroes that are not adjacent to other zeroes.
# The number of zeroes that are not adjacent to other zeroes is the number of zeroes that are at the beginning or end of the string.

# This means that the number of cubes that can be removed is the number of zeroes minus the number of zeroes that are at the beginning or end of the string.

zeroes = S.count("0")
zeroes_at_beginning_or_end = len(S) - len(S.lstrip("0").rstrip("0"))
print(zeroes - zeroes_at_beginning_or_end)
