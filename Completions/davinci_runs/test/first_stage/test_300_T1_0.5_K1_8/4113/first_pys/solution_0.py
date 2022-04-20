

# Read input
N = int(input())

# Check if N is odd
if N % 2 != 0:
    print('No')
else:
    # Check if N is a multiple of 4
    if N % 4 == 0:
        print('Yes')
    else:
        # Check if N is a multiple of 7
        if N % 7 == 0:
            print('Yes')
        else:
            # Check if N is a multiple of 11
            if N % 11 == 0:
                print('Yes')
            else:
                print('No')