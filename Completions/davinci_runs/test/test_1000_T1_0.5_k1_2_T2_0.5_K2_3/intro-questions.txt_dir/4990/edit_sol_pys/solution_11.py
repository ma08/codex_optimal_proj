

def main():
    # Get inputs
    b, k, g = [int(x) for x in input().split()] # b = number of bananas, k = number of bananas per day, g = number of bananas he gives to his friend
    # Calculate number of days
    days = (b - 1) // (k - g + 1) + 1
    # Print result
    print(days)

if __name__ == '__main__':
    main()
