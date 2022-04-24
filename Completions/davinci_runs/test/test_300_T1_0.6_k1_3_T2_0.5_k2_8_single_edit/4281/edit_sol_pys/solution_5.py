

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    
    # Sort the input array
    nums.sort()

    # Initialize the minimum and maximum result to be the sum of
    # the first and last elements of the array
    minimum = nums[0]
    maximum = nums[-1]

    # Initialize the count variable to be the number of elements with
    # the same value as the first element of the array
    count = 1
    for i in range(1, n):
        if nums[i] != nums[0]:
            break
        count += 1

    # The minimum number of occupied houses is the number of elements
    # that are equal to the first element of the array, because the
    # only way to reach the minimum number is to have all friends at
    # the house with the smallest coordinate
    minimum += count - 1

    # The maximum number of occupied houses is the number of elements
    # that are equal to the last element of the array, because the
    # only way to reach the maximum number is to have all friends at
    # the house with the largest coordinate
    count = 1
    for i in range(n - 1, 0, -1):
        if nums[i] != nums[-1]:
            break
        count += 1
    maximum += count - 1

    # Print the minimum and maximum result
    print(minimum, maximum)

if __name__ == "__main__":
    main()
