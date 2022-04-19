

def main():
    # Read input
    x, a = [int(i) for i in input().split()]

    # Compare the two values and print the result.
    print(0 if x < a else 10)

if __name__ == '__main__':
    main()
