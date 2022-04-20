

def solve(n):
    n = list(str(n))  # convert the number to a list of strings
    n = [int(i) for i in n]  # convert the strings to integers
    while len(n) > 1 and n[-1] == 0:  # remove the zeros from the end
        n = n[:-1]  # remove the last element
    if len(n) == 1:  # if the number is a single digit
        return 10
    else:  # if the number is more than one digit
        return len(n)


if __name__ == '__main__':
    n = int(input())
    print(solve(n))
