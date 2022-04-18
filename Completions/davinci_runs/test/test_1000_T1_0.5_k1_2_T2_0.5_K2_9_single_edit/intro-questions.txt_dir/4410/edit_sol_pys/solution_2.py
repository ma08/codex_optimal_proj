

# SOLUTION 1
# First we find the number of contiguous groups of 1's in the string.
# We do this by creating a list of the indices of where the 1's occur.
# Then we create a new list that contains the difference between each element
# of the first list, and the next. The number of contiguous groups of 1's is
# then the number of elements in this second list that are greater than k.

# Then we find the number of 1's in the string.

# The answer is the maximum of the two numbers.

# The time complexity of this solution is O(n)
# The space complexity of this solution is O(n)

def max_num_tables(n, k, s):
    indices = [i for i, x in enumerate(s) if x == "1"]
    differences = [indices[i + 1] - indices[i] for i in range(len(indices) - 1)]
    num_contiguous_groups = len([x for x in differences if x > k])
    num_ones = len(indices)
    return max(num_ones, num_contiguous_groups)


# SOLUTION 2
# First we find the number of contiguous groups of 1's in the string.
# We do this by keeping track of the number of 1's we have seen so far.
# We also keep track of the number of contiguous groups of 1's.
# The number of contiguous groups is incremented whenever we see a 0
# and the number of 1's we have seen so far is greater than 0.

# Then we find the number of 1's in the string.

# The answer is the maximum of the two numbers.

# The time complexity of this solution is O(n)
# The space complexity of this solution is O(1)

def max_num_tables_2(n, k, s):
    num_seen = 0
    num_contiguous_groups = 0
    for i in range(n):
        if s[i] == "1":
            num_seen += 1
        else:
            if num_seen > 0:
                num_contiguous_groups += 1
                num_seen = 0
    if num_seen > 0:
        num_contiguous_groups += 1
    return max(num_contiguous_groups, sum(int(x) for x in s))


num_tests = int(input().strip())
for _ in range(num_tests):
    n, k = map(int, input().split())
    s = input()
    print(max_num_tables(n, k, s))
