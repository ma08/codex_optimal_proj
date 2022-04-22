
S = input()

# The number of cubes that can be removed is the maximum number of zeros that are adjacent to ones.
# Since there can be at most 10^5 cubes, we can solve this problem in O(N) time.

# The number of zeros adjacent to ones is the number of zeros minus the number of zeros that are not adjacent to ones.
# The number of zeros that are not adjacent to ones is the number of zeros that are adjacent to other zeros.
# The number of zeros that are adjacent to other zeros is the number of zeros minus the number of zeros that are not adjacent to other zeros.
# The number of zeros that are not adjacent to other zeros is the number of zeros that are at the beginning or end of the string.

# This means that the number of cubes that can be removed is the number of zeros minus the number of zeros that are at the beginning or end of the string.

zeroes = S.count("0")
zeroes_at_beginning_or_end = len(S) - len(S.lstrip("0").rstrip("0"))
print(zeroes - zeroes_at_beginning_or_end)
