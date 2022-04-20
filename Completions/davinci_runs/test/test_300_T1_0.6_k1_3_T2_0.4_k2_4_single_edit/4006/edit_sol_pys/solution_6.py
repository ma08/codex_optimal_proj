

def solve(n):
    n = str(n)
    while len(n) > 1 and n[-1] == '0':
        n = n[:-1]  # remove the last element from the list
    if len(n) == 1:  # if there is only one element in the list
        return 10
    else:
        return len(n)


if __name__ == '__main__':
    n = int(input())
    print(solve(n))
