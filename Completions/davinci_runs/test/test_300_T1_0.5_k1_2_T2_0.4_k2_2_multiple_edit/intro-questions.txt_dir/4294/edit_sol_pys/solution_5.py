

def main():
    # Read the input
    x, a = [int(i) for i in input().split()]  # [int(i) for i in input().split()]

    # Compare the two values and print the result
    if x < a:
        print(0)
    else:
        print(10)

if __name__ == '__main__':
    main()
