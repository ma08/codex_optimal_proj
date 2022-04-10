

def main():

    # read input and save to a list of integers
    nums = list(map(int, input().split()))

    # sort the list
    nums.sort()

    # print 1 if all the elements are the same
    # it's enough to check the first and the last element,
    # because the list is sorted and the elements are 0 <= a_{i} <= 100
    print(1 if nums[0] == nums[-1] else 0)


if __name__ == '__main__':
    main()
