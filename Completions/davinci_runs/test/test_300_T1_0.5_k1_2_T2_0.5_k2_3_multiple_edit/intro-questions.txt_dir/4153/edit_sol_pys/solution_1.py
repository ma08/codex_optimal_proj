# The number of cubes that can be removed is the maximum number of zeros that are adjacent to ones.
# Since there can be at most 10^5 cubes, we can solve this problem in O(N) time.
# The number of zeros adjacent to ones is the number of zeros minus the number of zeros that are not adjacent to ones.
# The number of zeros that are not adjacent to ones is the number of zeros that are adjacent to other zeros.
# The number of zeros that are adjacent to other zeros is the number of zeros minus the number of zeros that are not adjacent to other zeros.
# The number of zeros that are not adjacent to other zeros is the number of zeros that are at the beginning or end of the string.
# This means that the number of cubes that can be removed is the number of zeros minus the number of zeros that are at the beginning or end of the string.

def solve():
    S = raw_input()
    zeros = S.count("0")
    zeros_at_beginning_or_end = len(S) - len(S.lstrip("0").rstrip("0"))
    print zeros - zeros_at_beginning_or_end

if __name__ == '__main__':
    solve()
