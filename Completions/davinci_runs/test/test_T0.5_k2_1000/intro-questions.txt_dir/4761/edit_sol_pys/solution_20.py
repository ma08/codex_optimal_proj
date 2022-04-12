

def main():
    low, high = [int(x) for x in input().split()]  # get the range
    num_combinations = 0
    for i in range(low, high + 1):  # iterate through the range
        if is_valid(i):  # if the number is valid
            num_combinations += 1

    print(num_combinations)

def is_valid(n):
    n = str(n)
    if len(n) != 6:
        return False
    if len(set(n)) != 6:
        return False
    for i in range(1, 10):
        if n.count(str(i)) > 1:
            return False
    for i in n:
        if int(n) % int(i) != 0:
            return False
    return True


main()
