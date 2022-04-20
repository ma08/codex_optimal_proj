

def main():
    n = int(input()) # number of houses
    x = list(map(int, input().split())) # coordinates of houses

    # sort the coordinates
    x.sort() 

    # initialize the minimum and maximum result to be the sum of the first and last elements of the array
    minimum = x[0] 
    maximum = x[-1] 

    # initialize the count variable to be the number of elements with the same value as the first element of the array
    count = 1 
    for i in range(1, n): 
        if x[i] != x[0]: 
            break 
        count += 1 

    # the minimum number of occupied houses is the number of elements that are equal to the first element of the array, because the only way to reach the minimum number is to have all friends at the house with the smallest coordinate
    minimum += count - 1 

    # the maximum number of occupied houses is the number of elements that are equal to the last element of the array, because the only way to reach the maximum number is to have all friends at the house with the largest coordinate
    count = 1 
    for i in range(n - 1, 0, -1): 
        if x[i] != x[-1]: 
            break 
        count += 1 
    maximum += count - 1 

    # print the minimum and maximum result
    print(minimum, maximum) 

if __name__ == "__main__":
    main()
