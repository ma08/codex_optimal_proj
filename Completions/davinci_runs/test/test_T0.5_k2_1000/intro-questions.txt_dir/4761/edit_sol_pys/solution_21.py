

def main():
    low, high = [int(x) for x in input().split()]  # get the range
    num_combinations = 0
    for i in range(low, high + 1):  # iterate through the range
        if is_valid(i):  # if the number is valid
            num_combinations += 1
    print(num_combinations)


def is_valid(n):
    pass


main()
