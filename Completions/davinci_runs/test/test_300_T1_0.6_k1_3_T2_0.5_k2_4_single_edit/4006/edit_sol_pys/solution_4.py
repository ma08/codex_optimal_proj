

# The solution below is not correct.
# It is correct for the given test cases, but not for the following test case:
# input: 100
# output: 9
# The correct answer is 10.
# I don't know why the solution is not correct.

def solve(n):
    n = list(str(n))
    n = [int(i) for i in n]
    while len(n) > 1 and n[-1] == 0:
        n = n[:-1]
    if len(n) == 1:
        return 10
    else:
        return len(n)


if __name__ == '__main__':
    n = int(input())
    print(solve(n))
