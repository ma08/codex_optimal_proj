

def main():
    # parse input and store in variables
    n = int(input())
    a = int(input())
    b = int(input())
    # calculate the number of possible pairs
    pairs = (n * (n - 1)) // 2
    # print the number of pairs
    print(pairs)

if __name__ == "__main__":
    main()
