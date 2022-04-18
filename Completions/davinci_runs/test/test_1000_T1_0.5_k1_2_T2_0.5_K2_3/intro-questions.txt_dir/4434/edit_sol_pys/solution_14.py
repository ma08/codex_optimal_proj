

def get_input():
    t = int(input())  # read a line with a single integer
    for i in range(t):
        n = int(input())  # read a list of integers, 2 in this case

        yield n  # use keyword yield instead of return in functions

def solve(n):
    if n == 1:
        return 0
    return (n - 1) ** 2


if __name__ == '__main__':
    for n in get_input():  # read input and call solve for each test case
        print(solve(n))
