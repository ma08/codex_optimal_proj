

def main():
    n = int(input())
    x = list(map(int, input().split()))
    
    # Sort the input array
    x.sort()

    # Initialize the minimum and maximum result to be the sum of
    # the first and last elements of the array
    minimum = x[0]
    maximum = x[-1]

    # Initialize the count variable to be the number of elements
    # in the array
    count = n

    # The minimum number of occupied houses is the number of
    # elements in the array, because the only way to reach the
    # minimum number is to have all friends at the house with the
    # smallest coordinate
    minimum += count

    # The maximum number of occupied houses is the number of
    # elements in the array, because the only way to reach the
    # maximum number is to have all friends at the house with the
    # largest coordinate
    maximum += count

    # Print the minimum and maximum result
    print(minimum, maximum)

if __name__ == "__main__":
    main()
