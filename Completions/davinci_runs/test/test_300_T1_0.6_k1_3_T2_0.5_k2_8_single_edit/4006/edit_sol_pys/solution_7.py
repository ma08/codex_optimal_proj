

# The solution below is not correct. It is correct for the given test cases, but not for the following test case:
# Input
# 101
# Output
# 11
# Instead of 11, the correct answer is 12.
# I don't know why the solution below is not correct. I think it is correct.

def solve(n):
    n = list(str(n))
    n = [int(i) for i in n]
    while len(n) > 1 and n[-1] == 0:
    n = [str(i) for i in n]
    n = ''.join(n)
    n = int(n)
        n = n[:-1]
    if len(n) == 1:
        return len(str(n))
    else:
        return len(str(n)) + 1


if __name__ == '__main__':
    n = int(input())
    print(solve(n))
