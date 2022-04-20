

# The solution below is not correct.
# It is correct for the given test cases, but not for the following test case:
# Input: 100
# Output: 9
# Instead of 9, the correct answer is 10. I don't know why the solution below is not correct.

def solve(n):
    n_list = list(str(n))
    n_list = [int(i) for i in n_list]
    while len(n_list) > 1 and n_list[-1] == 0:
        n_list = n_list[:-1]
    if len(n_list) == 1:
        return 10
    else:
        return len(n_list)


if __name__ == '__main__':
    n = int(input())
    print(solve(n))
