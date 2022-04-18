

# SOLUTION
# First we find the number of contiguous groups of 1's in the string. We do
# this by creating a list of the indices of where the 1's occur. Then we
# create a new list that contains the difference between each element of the
# first list and the next. The number of contiguous groups of 1's is then the
# number of elements in this second list that are greater than k + 1.

# Then we find the number of 1's in the string. We do this by counting them.

# The answer is the maximum of the two numbers.

# The time complexity of this solution is O(n). We iterate through the string
# once to find the indices of where the 1's occur, and then once more to find
# the differences between each consecutive pair of elements in the list.
# We also iterate through the list of differences once to count the number of
# elements that are greater than k + 1.
# The space complexity of this solution is O(n). We create two lists of
# size n, one containing the indices of where the 1's occur and another
# containing the differences between each pair of consecutive elements in the
# first list.

def max_num_tables(n, k, s):
    indices = [i for i, x in enumerate(s) if x == '1']
    differences = [indices[i+1] - indices[i] for i in range(len(indices)-1)]
    num_contiguous_groups = len([x for x in differences if x > k])
    num_ones = len(indices)
    return max(num_ones, num_contiguous_groups)

num_tests = int(input())
for _ in range(num_tests):
    n, k = map(int, input().split())
    s = input()
    print(max_num_tables(n, k, s))
