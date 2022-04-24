

# The solution below is not correct.
# It is correct for the given test cases, but not for the following test case:
# Input
# 100
# Output
# 9
# Instead of 9, the correct answer is 10.
# I don't know why the solution below is not correct.


def solve(n):
    n = list(str(n))
    n = [int(i) for i in n]
    return len(n)


if __name__ == '__main__':
    n = int(input())
    if n == 0:
        print(10)
    else:
        print(solve(n))
