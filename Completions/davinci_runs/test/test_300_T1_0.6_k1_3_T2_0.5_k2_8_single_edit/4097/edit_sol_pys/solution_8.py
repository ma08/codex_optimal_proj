
def solve(n, sequence):
    if n == 1 or n == 2:
        return 0
    else:
        diff = sequence[1] - sequence[0]  # difference between first two numbers
        for i in range(2, n):
            if sequence[i] - sequence[i-1] != diff:  # if difference is not equal to diff, return -1
                return -1  # return -1
        return 0  # return 0


if __name__ == '__main__':
    n = int(input())
    sequence = [int(x) for x in input().split()]
    print(solve(n, sequence))
