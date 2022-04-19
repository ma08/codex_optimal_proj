

def main():
    # Read inputs
    a, b, c = [int(i) for i in input().split()]

    # Compare the values and print the result.
    if a < b and b < c:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
