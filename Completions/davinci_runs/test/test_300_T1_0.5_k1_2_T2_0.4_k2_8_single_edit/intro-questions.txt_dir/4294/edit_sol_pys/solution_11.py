

def main():
    # Read input and split by spaces
    x, a = input().split()

    # Compare the two values and print the result
    if int(x) < int(a):
        print(0)
    else:
        print(10)

if __name__ == '__main__':
    main()
