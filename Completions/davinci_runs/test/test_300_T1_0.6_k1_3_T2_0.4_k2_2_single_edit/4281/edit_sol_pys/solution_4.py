

def main():
    n = int(input())
    x = list(map(int, input().split()))
    
    # Sort the input array
    x.sort()

    # Initialize the count variable to be the number of elements with
    # the same value as the first element of the array
    count = 1
    for i in range(1, n):
        if x[i] != x[0]:
            break
        count += 1

    # Print the minimum and maximum result
    print(minimum, maximum)

if __name__ == "__main__":
    main()
