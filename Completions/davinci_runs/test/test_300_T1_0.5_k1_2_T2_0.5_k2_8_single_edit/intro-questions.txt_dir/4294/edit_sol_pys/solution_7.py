

def main():
    # Read input
    x, a = [int(i) for i in input().split()] # input() returns a string, so we need to convert it to an int

    # Compare the two values and print the result.
    if x < a:
        print(0)
    else:
        print(10)

if __name__ == '__main__':
    main()
