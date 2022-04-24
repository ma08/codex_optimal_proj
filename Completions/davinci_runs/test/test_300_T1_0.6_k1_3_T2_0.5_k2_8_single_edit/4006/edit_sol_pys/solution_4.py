


def solve(n):
    n = list(str(n))  # convert n to list of characters
    n = [int(i) for i in n]  # convert each character to integer
    while len(n) > 1 and n[-1] == 0:  # remove trailing zeros
        n = n[:-1]  # remove last element of n
    if len(n) == 1:  # if length of n is 1, return 10
        return 10
    else:  # else return length of n
        return len(n)


if __name__ == '__main__':
    n = int(input())
    print(solve(n))
