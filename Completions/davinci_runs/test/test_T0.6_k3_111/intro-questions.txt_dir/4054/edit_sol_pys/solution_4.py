

def main():

    # read input and save to a list
    line = input()
    nums = list(map(int, line.split()))

    # sort the list
    nums.sort()

    # check if the elements are the same
    # it's enough to check the first and the last element,
    # because the list is sorted and the elements are 0 <= a_i <= 100
    if nums[0] == nums[-1]:
        # print 1 if all the elements are the same
        print(1)
    else:
        # print 0 otherwise
        print(0)


if __name__ == '__main__':
    main()
